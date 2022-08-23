from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from school.models import *
from teacher.models import *

# Create your models here.

class student_profile(models.Model):

    user =  models.OneToOneField(User, on_delete=models.CASCADE, null=True, unique=True, related_name="studentprofile")
    school = models.ForeignKey(School, null=True, on_delete=models.CASCADE, blank=True, unique=False, related_name="studentschoolprofile")
    img = models.ImageField(upload_to="students/", null=True, blank=True, default="s-avatar.jpg")
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True)

    dob = models.DateField()
    standard = models.IntegerField(null=True, blank=True)
    roll_no =  models.CharField(max_length=8, null=True, blank=True)
    section = models.CharField(max_length=8, null=True, blank=True)

    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)

    father_phone= models.CharField(max_length=50)
    mother_phone = models.CharField(max_length=50)

    address = models.TextField(blank=True, null=True)
    zipcode = models.IntegerField(null=True, blank=True)

    def __str__(self) :
        return self.full_name

        