"""intellify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from student import views


urlpatterns = [
    path('', views.dash, name='student'),
    path('list/', views.students, name='student_list'),
    path('add/', views.create_student, name='create_student'),
    path('login/', views.login_student, name='login_student'),
    path('logout/', views.logout_student, name='logout_student'),
    path('update/', views.edit_student, name='edit_student'),
    path('profile/', views.profile_student, name='profile_student'), # only teachers and students can access
    path('add/upload/', views.upload_student, name='upload_student'),
]
