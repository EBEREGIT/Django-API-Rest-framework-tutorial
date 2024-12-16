from django.shortcuts import render, HttpResponse
from rest_framework import status, mixins, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework.views import APIView


# Create your views here.
def home(request):
    return HttpResponse("Students API")


class Students(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

