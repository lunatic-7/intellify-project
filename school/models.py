from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# School Profile
# School Profile Model (Wasif)
class School(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    hod_name = models.CharField(max_length=100, default="")
    students_no = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)