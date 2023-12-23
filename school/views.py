from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from users.models import CustomUser, Profile

from .forms import SchoolForm, ClasseForm, MatiereForm, StudentForm
from .models import School, Classe, Matiere, Student


class SchoolCreateView(FormView):
    template_name = 'school/school_create.html'
    form_class = SchoolForm
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('school:dashboard'))
        
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        school_name = form.cleaned_data['name']
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        school, created = School.objects.get_or_create(name=school_name)      
        
        user = CustomUser.objects.create_user(username=username, password=password, is_staff=True, is_superuser=True, school=school)
        
        Profile.objects.create(user=user)

        messages.success(self.request, 'Compte a été créé ! Vous pouvez désormais vous connecter.')
        
        return super().form_valid(form)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'school/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school = self.request.user.school
        
        context['classes'] = Classe.objects.filter(school=school)
        context['matieres'] = Matiere.objects.filter(school=school)
        context['students'] = Student.objects.filter(school=school)
        
        return context


class ClasseCreateView(LoginRequiredMixin, CreateView):
    model = Classe
    form_class = ClasseForm
    template_name = 'school/classe_create.html'
    success_url = reverse_lazy('school:dashboard')

    def form_valid(self, form):
        form.instance.school = self.request.user.school
        return super().form_valid(form)


class ClasseUpdateView(LoginRequiredMixin, UpdateView):
    model = Classe
    form_class = ClasseForm
    template_name_suffix = "_update_form"


class ClasseDeleteView(LoginRequiredMixin, DeleteView):
    model = Classe
    success_url = reverse_lazy("school:dashboard")


class MatiereCreateView(LoginRequiredMixin, CreateView):
    model = Matiere
    form_class = MatiereForm
    template_name = 'school/matiere_create.html'
    success_url = reverse_lazy('school:dashboard')

    def form_valid(self, form):
        form.instance.school = self.request.user.school
        return super().form_valid(form)


class MatiereUpdateView(LoginRequiredMixin, UpdateView):
    model = Matiere
    form_class = MatiereForm
    template_name_suffix = "_update_form"


class MatiereDeleteView(LoginRequiredMixin, DeleteView):
    model = Matiere
    success_url = reverse_lazy("school:dashboard")


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student_create.html'
    success_url = reverse_lazy('school:dashboard')

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
    success_url = reverse_lazy("school:dashboard")