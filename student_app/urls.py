from django.urls import path
from .views import home, students, student_detail

urlpatterns = [
    path("", home, name="home"),
    path("students/", students, name="students"),
    path("students/<int:pk>", student_detail, name="student_detail"),
]
