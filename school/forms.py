from django import forms
from django.forms import ModelForm

from .models import School, Classe, Matiere, Student

class SchoolForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = School
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Personnalisation des champs avec des placeholders et sans label
        self.fields['name'].widget = forms.TextInput(attrs={
            'placeholder': 'Nom de l\'etablissement',
        })
        self.fields['name'].label = ''

        self.fields['username'].widget = forms.TextInput(attrs={
            'placeholder': 'Votre nom d\'utilisateur',
        })
        self.fields['username'].label = ''

        self.fields['password'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Votre mot de passe',
        })
        self.fields['password'].label = ''


class ClasseForm(ModelForm):
    class Meta:
        model = Classe
        fields = ['label']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['label'].label = 'Nom de la classe'
    

class MatiereForm(ModelForm):
    class Meta:
        model = Matiere
        fields = ['label']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['label'].label = 'Nom de la matiere'
    

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'birth_date', 'sex', 'classe']

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Nom de l\'eleve'
        self.fields['birth_date'].label = 'Date de naissance'
        self.fields['sex'].label = 'Sexe'
        
        if user and user.is_authenticated:
            # Filtrer le champ 'classe' pour n'afficher que les classes de l'utilisateur connecté
            self.fields['classe'].queryset = Classe.objects.filter(school=user.school)
