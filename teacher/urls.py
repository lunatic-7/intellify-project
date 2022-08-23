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
from teacher import views


urlpatterns = [
    path('', views.dash, name='teacher'),
    path('list/', views.teachers, name='teachers_list'),
    path('add/', views.create_teacher, name='create_teacher'),
    path('login/', views.login_teacher, name='login_teacher'),
    path('logout/', views.logout_teacher, name='logout_teacher'),
    path('update/', views.edit_teacher, name='edit_teacher'),
    path('profile/', views.profile_teacher, name='profile_teacher'), # only teachers and students can access
    path('add/upload/', views.upload_teacher, name='upload_teacher'),
]
