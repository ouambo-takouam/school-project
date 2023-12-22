from django.urls import reverse
from django.db import models
from django.utils import timezone

class School(models.Model):
    name = models.CharField(max_length=20)
    sigle = models.CharField(max_length=20, blank=True, null=True)
    adress = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Classe(models.Model):
    label = models.CharField(max_length=20, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.label
    
    def get_absolute_url(self):
        return reverse("school:home")


class Matiere(models.Model):
    label = models.CharField(max_length=20, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.label
    
    def get_absolute_url(self):
        return reverse("school:home")


class Student(models.Model):
    CHOICES = [
        ('girl', 'Fille'),
        ('boy', 'Garçon')
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    entry_date = models.DateField(default=timezone.now)
    sex = models.CharField(max_length=10, choices=CHOICES)
    registration_number = models.CharField(max_length=10, blank=True, null=True)
    active = models.BooleanField(default=True)
    
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
    
    def get_absolute_url(self):
        return reverse("school:home")
