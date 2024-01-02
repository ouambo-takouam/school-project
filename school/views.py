from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.views.generic.list import ListView
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
    

class ClasseListView(LoginRequiredMixin, ListView):
    model = Classe
    template_name = 'school/classe/classe_list.html'

    def get_queryset(self):
        current_user = self.request.user
        queryset = Classe.objects.filter(school=current_user.school)
        return queryset


class ClasseCreateView(LoginRequiredMixin, CreateView):
    model = Classe
    form_class = ClasseForm
    template_name = 'school/classe/classe_form.html'
    success_url = reverse_lazy('school:classe_list')

    def form_valid(self, form):
        form.instance.school = self.request.user.school
        return super().form_valid(form)


class ClasseUpdateView(LoginRequiredMixin, UpdateView):
    model = Classe
    form_class = ClasseForm
    template_name = 'school/classe/classe_form.html'


class ClasseDeleteView(LoginRequiredMixin, DeleteView):
    model = Classe
    template_name = 'school/classe/classe_confirm_delete.html'
    success_url = reverse_lazy("school:classe_list")


class MatiereListView(LoginRequiredMixin, ListView):
    model = Matiere
    template_name = 'school/matiere/matiere_list.html'

    def get_queryset(self):
        current_user = self.request.user
        queryset = Matiere.objects.filter(school=current_user.school)
        return queryset
    

class MatiereCreateView(LoginRequiredMixin, CreateView):
    model = Matiere
    form_class = MatiereForm
    template_name = 'school/matiere/matiere_form.html'
    success_url = reverse_lazy('school:matiere_list')

    def form_valid(self, form):
        form.instance.school = self.request.user.school
        return super().form_valid(form)


class MatiereUpdateView(LoginRequiredMixin, UpdateView):
    model = Matiere
    form_class = MatiereForm
    template_name = 'school/matiere/matiere_form.html'


class MatiereDeleteView(LoginRequiredMixin, DeleteView):
    model = Matiere
    template_name = 'school/matiere/matiere_confirm_delete.html'
    success_url = reverse_lazy("school:matiere_list")


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'school/student/student_list.html'

    def get_queryset(self):
        current_user = self.request.user
        queryset = Student.objects.filter(school=current_user.school)
        return queryset


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student/student_form.html'
    success_url = reverse_lazy('school:student_list')

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
    template_name = 'school/student/student_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'school/student/student_confirm_delete.html'
    success_url = reverse_lazy("school:student_list")