from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.name}"

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.name}"

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,null=True, blank=True, related_name="students")
    subjects = models.ManyToManyField(Subject, related_name="students")
    document = models.FileField(upload_to="documents/", blank=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True)

    def __str__(self):
        return f"{self.id} {self.name} {self.age}"

class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE,null=True,blank=True, related_name="profile")
    phone_no = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} - {self.phone_no}"

# from students.models import Student, StudentProfile, Course, Subject
# student = Student.objects.get(id=1)
# course = Course.objects.get(id=1)
# subject = Subject.objects.get(id=1)

# student.course = course
# student.save()

# ADD

# Model : 
# Course : name
# Subject: name
# StudentProfile: student,phone_no

# Relationship

# Course -> Student
# BCA -> Ram, Shyam, others
# BIT -> Hari, Gopal, other
# 1 <-> Many Relationship

# Student table
# id Name course_id
# 1  ram  1
# 2 hari  1
# 3 shyam 2

# Subject -> Student
# Math -> Ram, Hari
# CProgramming -> Ram, Hari, Gopal, Shyam
# Many <-> Many Relationship

# Pivot table
# id, subject_id, student_id
# 1 ,     math          ram
# 2       math          hari
# 3       CProgram      ram
# 4       CProgram      hari
# 5       CProgram      shyam
# 6       CProgram      gopal  


# student  -> StudentProfile
#     Ram   -> 2015-08-23,9893879898  
#     Shyam -> 2014-06-09,9876543233
#     1 <-> 1 Relationship

# StudentProfile table:
# id student_id   dob.        phone_number
# 1   1           2015-08-23  9893879898