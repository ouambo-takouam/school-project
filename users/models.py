from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models

from school.models import School

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("users:list")

class Profile(models.Model):
    CHOICES = [
        ('admin', 'Administrateur'),
        ('teacher', 'Enseignant')
    ]
    
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    role = models.CharField(max_length=50, choices=CHOICES, default='admin')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    @property
    def display_role(self):
        return dict(self.CHOICES).get(self.role, 'Undefined')
