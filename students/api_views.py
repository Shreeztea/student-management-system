from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer


class CourseListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        students = Course.objects.all()
        serializer = CourseSerializer(students, many=True)

        return Response(serializer.data)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ["age", "course"]
    search_fields = ["name", "email", "address"]
    ordering_fields = ["name", "age"]
    ordering = ["id"]



# from rest_framework import generics
# class StudentListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer







