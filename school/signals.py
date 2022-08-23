from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import School
from teacher.models import teacher_profile
from django.contrib.auth.models import Group

# Creating school profile whenever a school user is created and alloting them to their respective group.
# (Wasif)

# def school_profile(sender, instance, created, **kwargs):
#     if created:
#         group = Group.objects.get(name="school")
#         instance.groups.add(group)
            
#         School.objects.create(user=instance, name=instance.username)

#         print("Profile Created")

# post_save.connect(school_profile, sender=User)

