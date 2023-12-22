from django.urls import path

from . import views
from .views import (
    ClasseCreateView,
    ClasseUpdateView, 
    ClasseDeleteView, 
    MatiereCreateView,
    MatiereUpdateView,
    MatiereDeleteView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView
)

app_name = 'school'

urlpatterns = [
    path('', views.home, name='home'),

    path('classes/create/', ClasseCreateView.as_view(), name='create_classe'),
    path('classes/<int:pk>/update/', ClasseUpdateView.as_view(), name='update_classe'),
    path('classes/<int:pk>/delete/', ClasseDeleteView.as_view(), name='delete_classe'),
    
    path('matieres/create/', MatiereCreateView.as_view(), name='create_matiere'),
    path('matieres/<int:pk>/update/', MatiereUpdateView.as_view(), name='update_matiere'),
    path('matieres/<int:pk>/delete/', MatiereDeleteView.as_view(), name='delete_matiere'),

    path('students/create/', StudentCreateView.as_view(), name='create_student'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='update_student'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='delete_student'),
]
