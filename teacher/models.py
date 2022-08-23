from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from school.models import School


# Create your models here.


class teacher_profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE, null=True, unique=True, related_name="teacherprofile")
    school = models.ForeignKey(School, null=True, on_delete=models.CASCADE, blank=True, unique=False, related_name="schoolprofile")
    img = models.ImageField(upload_to="teachers/", null=True, blank=True, default="t-avatar.jpg")
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=50, blank=True)
    qualification = models.CharField(max_length=100, blank=True)
    experience = models.TextField(blank=True)
    address = models.TextField(blank=True)
    zipcode = models.IntegerField(max_length=6, blank=True, null=True)

    def __str__(self) :
        return self.full_name