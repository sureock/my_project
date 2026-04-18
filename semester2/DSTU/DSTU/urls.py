"""
URL configuration for DSTU project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from catalog import views

urlpatterns = [
    path("logout/",
         LogoutView.as_view(template_name='logged_out.html'),
         name='logout'),
    path("login/",
         LoginView.as_view(template_name='login.html'),
         name='login'),
    path("", views.index),
    path("info/<str:name>", views.info),
    path("404", views.not_found),
    path('authors/create/', views.create_author),
    path('authors/update/<int:teacher_id>/', views.update_authors),
    path('authors/delete/<int:teacher_id>/', views.delete_authors, name='delete_author'),
    path("authors/", views.index_authors),
    path("authors/<int:teacher_id>/", views.info_authors),
    path('courses/create/', views.create_course),
    path('courses/update/<int:course_id>/', views.update_courses),
    path('courses/delete/<int:course_id>/', views.delete_courses, name='delete_course'),
    path("courses/", views.index_course),
    path("courses/<int:teacher_id>/", views.info_course),
    path('students/create/', views.create_students),
    path('students/update/<int:student_id>/', views.update_students),
    path('students/delete/<int:student_id>/', views.delete_students, name='delete_student'),
    path("students/", views.index_student),
    path('students/sign/<int:student_id>/', views.sign_students),
    path('students/unsign/<int:student_id>/', views.unsign_students, name='unsign_student'),
    path('orm/', views.orm_field),
    # re_path(r"^courses", views.courses),
]
