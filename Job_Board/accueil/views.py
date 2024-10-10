from django.shortcuts import render, redirect
from django.contrib import messages
from .models import People
from django.db import IntegrityError

def home(request):
    return render(request, 'accueil/index.html')



def student_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password') 
        education_level = request.POST.get('education_level')  

        if People.objects.filter(email=email).exists():
            messages.error(request, 'Cet email est déjà utilisé.')
        else:
            try:
                person = People.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    role='applicant'  
                )
                person.save()

                messages.success(request, 'Inscription réussie. Vous pouvez vous connecter.')
                return redirect('login')  
            except IntegrityError:
                messages.error(request, 'Une erreur est survenue lors de la création de votre compte.')
    
    return render(request, 'accueil/inscription.html')


def login_view(request):
    
    return render(request, 'accueil/login.html')