from django.urls import path
from .views import home, Students, StudentDetail

urlpatterns = [
    path("", home, name="home"),
    path("students/", Students.as_view(), name="students"),
    path("students/<int:pk>", StudentDetail.as_view(), name="student_detail"),
]
