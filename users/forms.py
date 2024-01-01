from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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


class UserProfileForm(UserCreationForm):
    phone = forms.CharField(label='Numéro de téléphone', max_length=20)
    role = forms.ChoiceField(label='Rôle', choices=Profile.CHOICES)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'phone']
        labels = {
            'username': 'Nom d\'utilisateur',
            'email': 'Adresse e-mail'
        }

    def save(self, school, commit=True):
        user = super().save(commit=False)
        user.phone = self.cleaned_data['phone']
        user.school = school
        if commit:
            user.save()

            profile = Profile.objects.create(
                user=user,
                role=self.cleaned_data['role']
            )
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'phone']
        labels = {
            'first_name': 'Nom',
            'last_name': 'Prenom',
            'username': 'Nom d\'utilisateur',
            'email': 'Adresse e-mail',
            'phone': 'Numéro de téléphone'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget = forms.TextInput(attrs={
            'placeholder': 'william@example.com'
        })

        self.fields['phone'].widget = forms.TextInput(attrs={
            'placeholder': '+1452 876 5432'
        })


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }