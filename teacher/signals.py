# from django.db.models.signals import post_save

# from django.contrib.auth.models import User, Group
# from .models import teacher_profile
# from school.models import School


# # create a teacher profile when teacher account is created
# # Ayon
# def teacher_profile_creation(sender, instance, created, **kwargs):
#     if created:
#         instance.groups.add(Group.objects.get(name="teachers"))
#         teacher_profile.objects.create(
#             user = instance, # teacher's user account
#             full_name = instance.first_name + instance.last_name,
#         )
# post_save.connect(teacher_profile_creation, sender=User)
