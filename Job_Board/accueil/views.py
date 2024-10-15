from django.shortcuts import render, redirect
from django.contrib import messages
from .models import People
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password

def home(request):
    return render(request, 'accueil/index.html')

def student_signup(request):
    if request.method == 'POST':
        
        first_name = request.POST.get('first_name')  
        last_name = request.POST.get('last_name')  
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        
        if password != password_confirm:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
            return render(request, 'accueil/inscription.html')

        
        if People.objects.filter(email=email).exists():
            messages.error(request, 'Cet email est déjà utilisé.')
            return render(request, 'accueil/inscription.html')

        try:
            
            person = People.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=make_password(password),  
                role='applicant',  
                company_id=None  
            )
            person.save()

            messages.success(request, 'Inscription réussie. Vous pouvez vous connecter.')
            return redirect('login')  
        except IntegrityError:
            messages.error(request, 'Une erreur est survenue lors de la création de votre compte.')
    
    return render(request, 'accueil/inscription.html')



def login_view(request):
    return render(request, 'accueil/login.html')

def inscription_view(request):
    return render(request, 'inscription.html')