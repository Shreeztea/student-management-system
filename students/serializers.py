from rest_framework import serializers
from .models import Student, Course
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id","name","email","age","address"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["name"]