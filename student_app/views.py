from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer


# Create your views here.
def home(request):
    return HttpResponse("Students API")


@api_view(["GET", "POST"])
def students(request):
    if request.method == "GET":
        students = Student.objects.all()
        return Response(
            StudentSerializer(students, many=True).data, status=status.HTTP_200_OK
        )

    if request.method == "POST":
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response(student.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def student_detail(request, pk):
    student_detail = Student.objects.get(pk=pk)

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
