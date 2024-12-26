from django.urls import path
from .views import home, students, student_detail, login, register, logout

urlpatterns = [
    path("", home, name="home"),
    path("students/", students, name="students"),
    path("students/<int:pk>", student_detail, name="student_detail"),
    
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
]
