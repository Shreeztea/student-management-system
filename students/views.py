import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required

from .forms import StudentForm
from .models import AIConversation,Student, Course
from .ai_service import ask_ai

def ai_chat(request):
    answer = ""
    error = ""
    question = ""

    if request.method == "POST":
        question = request.POST.get("question","").strip()
        if question:
            try:
                answer = ask_ai(question)
                AIConversation.objects.create(question=question,answer=answer)
            except Exception:
                error = "Sorry, the AI service is unavailable"

    converations = AIConversation.objects.order_by("-created_at")
    context = {
            'header' : 'AI Chat Assistant',
            'title': 'AI Chat Assistant',
            'answer': answer,
            'question': question,
            'error': error,
            'conversations': converations
        }
    return render(request, "students/ai_chat.html", context)



def add_course(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        course = Course.objects.create(name = request_data["name"])

        data = {
            "id": course.id,
            "name": course.name
        }
        return JsonResponse(data, status=200)


def get_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        data = {
            "id": course.id,
            "name": course.name
        }
        return JsonResponse(data, status=200)
    except Course.DoesNotExist:
        return JsonResponse({}, status=404)

def home(request):
    # return HttpResponse("Hello Django!")
    context = {
        'title' : 'Student System',
        'header': 'Student Management System',
        'paragraphs' : ['This is the first para', 'This is the second para','This is the third para'],
        'login' : True
    }

    return render(request, "students/home.html", context)

def list_courses(request):
    courses = Course.objects.all()

    context = {
        'header' : 'Course List',
        'title': 'Courses',
        'courses': courses
    }

    return render(request, "students/list_course.html",context)

def list_students(request):
    students = Student.objects.all()

    context = {
        'header' : 'Student List',
        'title': 'Students',
        'students': students
    }

    return render(request, "students/list_student.html",context)
    
def view_student(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {
        'header' : 'Student Detail',
        'title': 'Student Detail',
        'student': student
    }

    return render(request, "students/view_student.html",context)

@permission_required('students.add_student')
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
        
    context = {
        'header' : 'Add Student',
        'title': 'Add Student',
        'form': form
    }

    return render(request, "students/add_student.html",context)
# def add_student(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         age = request.POST.get("age")
#         address = request.POST.get("address")
#         course_id = request.POST.get("course_id")

#         Student.objects.create(name=name, email=email, age=age, address=address, course_id=course_id)

#         return redirect('students')
#     else:
#         courses = Course.objects.all()
#         context = {
#             'header' : 'Add Student',
#             'title': 'Add Student',
#             'courses': courses
#         }

#         return render(request, "students/add_student.html",context)

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('students')

def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm(instance=student)

    context = {
        'header' : 'Edit Student',
        'title': 'Edit Student',
        'form': form
    }

    return render(request, "students/add_student.html",context)