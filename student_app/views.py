from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer, UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def home(request):
    return HttpResponse("Students API")


@api_view(["POST"])
def login(request):
    user = User.objects.get(username=request.data["username"])

    if user.check_password(request.data["password"]):
        token = Token.objects.create(user=user)
        return Response(
            {"message": "Login Success", "token": token.key}, status=status.HTTP_200_OK
        )


@api_view(["POST"])
def register(request):
    user = UserSerializer(data=request.data)

    if user.is_valid():
        user.save()

        userRetrieved = User.objects.get(username=user.data["username"])
        userRetrieved.set_password(user.data["password"])

        userRetrieved.save()

        return Response(user.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def logout(request):
    Token.objects.get(key=request.data["token"]).delete()
    return Response({"message": "Logout Success"}, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def students(request):
    if request.method == "GET":
        students = Student.objects.filter(owner=request.user)
        return Response(
            StudentSerializer(students, many=True).data, status=status.HTTP_200_OK
        )

    if request.method == "POST":
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save(owner=request.user)
            return Response(student.data, status=status.HTTP_201_CREATED)



@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def student_detail(request, pk):
    student_detail = Student.objects.get(pk=pk)

    if student_detail.owner.username != request.user.username:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "GET":
        return Response(
            StudentSerializer(student_detail).data, status=status.HTTP_200_OK
        )

    if request.method == "PUT":
        student = StudentSerializer(student_detail, data=request.data)
        if student.is_valid():
            student.save()
            return Response(student.data, status=status.HTTP_202_ACCEPTED)

    if request.method == "DELETE":
        student_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
