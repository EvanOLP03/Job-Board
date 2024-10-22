from django import forms
from .models import People
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume', 'cover_letter_file']  
        widgets = {
            'resume': forms.FileInput(attrs={'class': 'form-control'}),
            'cover_letter_file': forms.FileInput(attrs={'class': 'form-control'}),  
        }

class StudentSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmez le mot de passe")

    class Meta:
        model = People
        fields = ['first_name', 'last_name', 'email', 'phone']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        
        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')

from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'salary_min', 'salary_max', 'job_type', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du poste'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'entreprise'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lieu'}),
            'salary_min': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salaire minimum'}),
            'salary_max': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salaire maximum'}),
            'job_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type de poste'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description du poste'}),
        }
