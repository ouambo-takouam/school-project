from django.urls import path

from .views import (
    DashboardView,
    SchoolCreateView,
    ClasseListView,
    ClasseCreateView,
    ClasseUpdateView, 
    ClasseDeleteView, 
    MatiereListView,
    MatiereCreateView,
    MatiereUpdateView,
    MatiereDeleteView,
    StudentListView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView
)

app_name = 'school'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    
    path('school/create', SchoolCreateView.as_view(), name='school_create'),

    path('classes/list/', ClasseListView.as_view(), name='classe_list'),
    path('classes/create/', ClasseCreateView.as_view(), name='classe_create'),
    path('classes/<int:pk>/update/', ClasseUpdateView.as_view(), name='classe_update'),
    path('classes/<int:pk>/delete/', ClasseDeleteView.as_view(), name='classe_delete'),
    
    path('matieres/list/', MatiereListView.as_view(), name='matiere_list'),
    path('matieres/create/', MatiereCreateView.as_view(), name='matiere_create'),
    path('matieres/<int:pk>/update/', MatiereUpdateView.as_view(), name='matiere_update'),
    path('matieres/<int:pk>/delete/', MatiereDeleteView.as_view(), name='matiere_delete'),

    path('students/list/', StudentListView.as_view(), name='student_list'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
]
