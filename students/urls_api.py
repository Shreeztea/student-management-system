from django.urls import path
from rest_framework.routers import DefaultRouter
from .api_views import StudentViewSet, CourseListAPIView


router = DefaultRouter()

router.register("students", StudentViewSet, basename="student")


urlpatterns = [
    path("course/", CourseListAPIView.as_view(), name= "student-list"),
]

urlpatterns += router.urls
