from django import forms
from django.contrib.auth.forms import AuthenticationForm

from school.models import School
from .models import CustomUser, Profile


class LoginAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Personnalisation du champ username avec un placeholder et sans label
        self.fields['username'].widget = forms.TextInput(attrs={
            'placeholder': 'Votre nom d\'utilisateur'
        })

        # Suppression de l'étiquette (label) associée au champ username
        self.fields['username'].label = ''

        # Personnalisation du champ password avec un placeholder et sans label
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Votre mot de passe'
        })

        # Suppression de l'étiquette (label) associée au champ password
        self.fields['password'].label = ''

    
class UserProfileForm(forms.ModelForm):
    role = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'phone']

    def save(self, school, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.school = school

        if commit:
            user.set_password(password)
            user.save()
            
            profile = Profile.objects.create(user=user, role=self.cleaned_data['role'])
            profile.save()

        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        labels = {
            'username': 'Nom d\'utilisateur',
            'email': 'Adresse e-mail'
        }