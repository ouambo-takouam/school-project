from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from school.models import School

from .forms import LoginAuthenticationForm, SchoolForm, UserProfileForm, UserUpdateForm
from .models import CustomUser, Profile
from .mixins import RedirectAuthenticatedUserMixin


class CustomLoginView(RedirectAuthenticatedUserMixin, LoginView):
    form_class = LoginAuthenticationForm
    template_name = 'users/login.html'

def create_school(request):
    if request.user.is_authenticated:
        return redirect('school:home')
    
    if request.method == 'POST':
        form = SchoolForm(request.POST)

        if form.is_valid():
            # Recuperation des donnees du formulaire
            school_name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Vérifier si l'école existe déjà ou creer une nouvelle
            school, created = School.objects.get_or_create(name=school_name)
            
            user = CustomUser.objects.create_user(username=username, password=password, is_staff=True, is_superuser=True, school=school)

            # Création du profil associé à l'utilisateur avec le rôle admin actif par defaut
            Profile.objects.create(user=user)

            messages.success(request, 'Compte a été créé ! Vous pouvez désormais vous connecter.')

            return redirect('login')

    else:
        form = SchoolForm()

    return render(request, 'users/create_school.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid():
            u_form.save()
            # p_form.save()
            messages.success(request, 'Votre compte a été mis à jour.')

            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    return render(request, 'users/profile.html', {'u_form': u_form})


def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():
            form.save(school=request.user.school)
            return redirect('school:home')

    else:
        form = UserProfileForm()

    return render(request, 'users/create_profile.html', {'form': form})