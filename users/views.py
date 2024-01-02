from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import LoginAuthenticationForm, UserAccountForm, UserForm, ProfileForm
from .mixins import RedirectAuthenticatedUserMixin
from .models import CustomUser


class CustomLoginView(RedirectAuthenticatedUserMixin, LoginView):
    form_class = LoginAuthenticationForm
    template_name = 'users/login.html'

class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'users/logout.html'

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        print(request.FILES)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Votre compte a été mis à jour.')

            return redirect('profile')
    else:
        u_form = UserForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {
        'u_form': u_form,
        'p_form': p_form
    })


class UserCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    template_name = 'users/user_form.html'
    form_class = UserAccountForm
    success_url = reverse_lazy('users:list')

    def form_valid(self, form):
        form.instance.school = self.request.user.school
        return super().form_valid(form)
    

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserAccountForm
    template_name = 'users/user_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['is_update'] = True  # Pass is_update as True because updating
        
        if 'school' in kwargs:
            del kwargs['school']  # Exclude 'school' argument
        
        return kwargs
    

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy("users:list")


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'users/user_list.html'

    def get_queryset(self):
        current_user = self.request.user
        queryset = CustomUser.objects.filter(school=current_user.school)
        return queryset