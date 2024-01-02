from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from school.models import School
from .models import CustomUser, Profile


class LoginAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Personnalisation des champs avec placeholder et sans label
        self.fields['username'].widget = forms.TextInput(attrs={
            'placeholder': 'Votre nom d\'utilisateur'
        })
        self.fields['username'].label = ''

        self.fields['password'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Votre mot de passe'
        })
        self.fields['password'].label = ''


class UserAccountForm(forms.ModelForm):
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput, required=False)
    phone = forms.CharField(label='Numéro de téléphone', max_length=20)
    role = forms.ChoiceField(label='Rôle', choices=Profile.CHOICES)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'phone']
        labels = {
            'username': 'Nom d\'utilisateur',
            'email': 'Adresse e-mail'
        }

    def __init__(self, *args, **kwargs):
        self.school = kwargs.pop('school', None)  # Retrieve 'school' from kwargs
        is_update = kwargs.pop('is_update', False)  # Check if it's an update
        super().__init__(*args, **kwargs)
        self.fields['phone'].required = True  # Make phone field required
        self.fields['password'].required = False  # Allow password field to be optional for updates

        if is_update:
            # Exclude password field when updating an existing user
            self.fields.pop('password')

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get('password'):
            user.set_password(self.cleaned_data['password'])
            user.phone = self.cleaned_data['phone']
        
        if self.school:  # Check if 'school' is provided (for creating new users)
            user.school = self.school
        
        if commit:
            user.save()
            profile, created = Profile.objects.get_or_create(
                user=user,
                defaults={'role': self.cleaned_data['role']}
            )
            
            if not created:
                profile.role = self.cleaned_data['role']
                profile.save()
                
        return user


class UserForm(forms.ModelForm):
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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }