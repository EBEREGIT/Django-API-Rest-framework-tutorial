from django.urls import path, include
from .views import home, Students
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"students", Students, basename="students")
urlpatterns = [
    path("", home, name="home"),
    path("", include(router.urls)),
]
