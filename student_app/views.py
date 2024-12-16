from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework.views import APIView


# Create your views here.
def home(request):
    return HttpResponse("Students API")


class Students(APIView):
    def get(self, request, format=None):
        students = Student.objects.all()
        return Response(
            StudentSerializer(students, many=True).data, status=status.HTTP_200_OK
        )

    def post(self, request, format=None):
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response(student.data, status=status.HTTP_201_CREATED)


class StudentDetail(APIView):

    def student_detail(self, pk):
        return Student.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        return Response(
            StudentSerializer(self.student_detail(pk)).data, status=status.HTTP_200_OK
        )

    def put(self, request, pk, format=None):
        student = StudentSerializer(self.student_detail(pk), data=request.data)
        if student.is_valid():
            student.save()
            return Response(student.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk, format=None):
        self.student_detail(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
