from django.contrib.auth.models import AbstractUser
from django.db import models

from school.models import School

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class Profile(models.Model):
    CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher')
    ]
    
    role = models.CharField(max_length=50, choices=CHOICES, default='admin')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}\'s profile'
