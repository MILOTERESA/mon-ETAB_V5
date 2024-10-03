from school.models.school import SchoolModel
from django.db import models



from django.contrib.auth.models import AbstractUser
from .role_user import RoleUserModel

# Create your models here.
class CustomUserModel(AbstractUser):
    role = models.ManyToManyField(RoleUserModel)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE, null=True, blank=True)


    
