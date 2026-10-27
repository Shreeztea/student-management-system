"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from drf_spectacular.views import (SpectacularAPIView,SpectacularSwaggerView,SpectacularRedocView)

from django.contrib import admin
from django.urls import path, include
from students.views import ai_chat,add_course,add_student,get_course, home, list_courses, list_students, view_student, edit_student, delete_student
from accounts.views import register,profile

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("students.urls_api")),
    path("", home, name="home"),
    path("students/", list_students, name="students"),
    path("students/add/", add_student, name="add_student"),
    path("students/<int:student_id>/", view_student, name="view_student"),
    path("students/edit/<int:student_id>/", edit_student, name="edit_student"),
    path("students/delete/<int:student_id>", delete_student, name="delete_student"),

    path("register/", register, name="register"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("accounts/profile/",profile,name="profile"),

    path("courses/", list_courses, name="courses"),
    path("course/get/<int:course_id>/",get_course,name="get_course"),
    path("course/add/",add_course,name="add_course"),

    path("api/schema/",SpectacularAPIView.as_view(),name="schema",),
    path("api/docs/",SpectacularSwaggerView.as_view(url_name="schema"),name="swagger-ui",),
    path("api/redoc/",SpectacularRedocView.as_view(url_name="schema"),name="redoc",),

    path("ai-chat/", ai_chat, name="ai_chat"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
