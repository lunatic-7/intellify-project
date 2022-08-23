from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages

from .models import *
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required

# Create your views here.

# School Dashboard (Wasif)
@login_required(login_url='school_login')
@allowed_users(allowed_roles=['school', 'admin'])
def schoolHome(request):
    school_name = request.user
    school_id = request.user.school.id
    print(school_name)
    context = {'school_name': school_name, 'school_id': school_id}
    return render(request, 'school/index.html', context)

# School Registration (Wasif)
@unauthenticated_user
def schoolRegister(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST["username"]
        fname = request.POST["school_name"]
        email = request.POST["school_email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        # Check for errorneous inputs
        if not username.isalnum() or len(username) > 10:
            messages.error(request, 'Your username should be alphanumeric and less than 10 characters!')
            return redirect("school_register")

        if pass1 != pass2:
            messages.error(request, 'Passwords did not match!')
            return redirect("school_register")

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.save()

        Group.objects.get(name='school').user_set.add(myuser)
        School.objects.create(user=myuser, name=myuser.username)

        messages.success(request, "Account created, Now you can log in to your account!")
        return redirect("school_login")
    return render(request, "school/register.html")

# School Login (Wasif)
@unauthenticated_user
def schoolLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
          
            return redirect("school_home")
        else:
            messages.error(request, "Invalid Credentials!")
            return redirect("school_login")
        
    return render(request, "school/login.html")

# School Logout (Wasif)
def schoolLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect("school_login")

# Edit/Add School Profile (Wasif)
@login_required(login_url='school_login')
@allowed_users(allowed_roles=['school', 'admin'])
def schoolProfileAdd(request):
    if request.method == "POST":
        # Get the post parameters
        school_head = request.POST["school_head"]
        phone_no = request.POST["phone_no"]
        students_no = request.POST["students_no"]
        email = request.POST["email"]
        school_name = request.POST["school_name"]
        print(school_head)

        profile = request.user.school.id
        s_profile = School.objects.filter(id=profile).update(hod_name=school_head, students_no=students_no, phone=phone_no, email=email, name=school_name)
        return redirect("school_profile")

    s_profile = request.user.school
    print(s_profile)
    context = {'s_profile': s_profile, 'school_id' : request.user.school.id}
    return render(request, 'school/school_profile_add.html', context)

# School Profile Page (Wasif)
@login_required(login_url='school_login')
@allowed_users(allowed_roles=['school', 'admin'])
def schoolProfile(request):
    s_profile = request.user.school
    print(s_profile)
    context = {'s_profile': s_profile, 'school_id' : request.user.school.id}
    return render(request, 'school/school_profile.html', context)