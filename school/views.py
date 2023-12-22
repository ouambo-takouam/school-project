from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import ClasseForm, MatiereForm, StudentForm
from .models import Classe, Matiere, Student

@login_required
def home(request): #dashboard
    classes = Classe.objects.filter(school=request.user.school)
    matieres = Matiere.objects.filter(school=request.user.school)
    students = Student.objects.filter(school=request.user.school)
    
    return render(request, 'school/home.html', {
        'classes': classes,
        'matieres': matieres,
        'students': students
    })


class ClasseCreateView(LoginRequiredMixin, CreateView):
    model = Classe
    form_class = ClasseForm
    template_name = 'school/classe_create.html'
    success_url = reverse_lazy('school:home')

    def form_valid(self, form):
        form.instance.school = self.request.user.school
        return super().form_valid(form)


class ClasseUpdateView(LoginRequiredMixin, UpdateView):
    model = Classe
    form_class = ClasseForm
    template_name_suffix = "_update_form"


class ClasseDeleteView(LoginRequiredMixin, DeleteView):
    model = Classe
    success_url = reverse_lazy("school:home")


class MatiereCreateView(LoginRequiredMixin, CreateView):
    model = Matiere
    form_class = MatiereForm
    template_name = 'school/matiere_create.html'
    success_url = reverse_lazy('school:home')

    def form_valid(self, form):
        form.instance.school = self.request.user.school
        return super().form_valid(form)


class MatiereUpdateView(LoginRequiredMixin, UpdateView):
    model = Matiere
    form_class = MatiereForm
    template_name_suffix = "_update_form"


class MatiereDeleteView(LoginRequiredMixin, DeleteView):
    model = Matiere
    success_url = reverse_lazy("school:home")


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student_create.html'
    success_url = reverse_lazy('school:home')

    def form_valid(self, form):
        form.instance.school = self.request.user.school
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Passez l'utilisateur connecté au formulaire
        return kwargs


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name_suffix = "_update_form"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("school:home")