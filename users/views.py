from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from .forms import LoginAuthenticationForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm
from .mixins import RedirectAuthenticatedUserMixin
from .models import CustomUser


class CustomLoginView(RedirectAuthenticatedUserMixin, LoginView):
    form_class = LoginAuthenticationForm
    template_name = 'users/login.html'


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        print(request.FILES)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Votre compte a été mis à jour.')

            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {
        'u_form': u_form,
        'p_form': p_form
    })


def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():
            form.save(school=request.user.school)
            return redirect('school:dashboard')

    else:
        form = UserProfileForm()

    return render(request, 'users/create_profile.html', {'form': form})


class UsersListView(ListView):
    model = CustomUser
    template_name = 'users/users_list.html'