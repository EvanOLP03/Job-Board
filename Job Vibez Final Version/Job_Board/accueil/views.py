from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.decorators import login_required
from .models import People, Job, Company
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password
from .forms import ApplicationForm

# Page d'accueil
def home(request):
    return render(request, 'accueil/index.html')  



# Vue pour l'inscription d'un utilisateur
def student_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')  
        last_name = request.POST.get('last_name')  
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        role = request.POST.get('role')  

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
                role=role,  
                company_id=None  
            )
            person.save()

            messages.success(request, 'Inscription réussie. Vous pouvez vous connecter.')
            return redirect('login')  
        except IntegrityError:
            messages.error(request, 'Une erreur est survenue lors de la création de votre compte.')

    return render(request, 'accueil/inscription.html')


# Vue pour gérer la connexion
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)  
            
            if user.role == 'recruiter':
                return redirect('recruiter_profile')  
            else:
                return redirect('profile')  
            
        else:
            
            messages.error(request, 'Email ou mot de passe incorrect.')
    
    return render(request, 'accueil/login.html')


# Vue pour déconnecter l'utilisateur
def logout_view(request):
    logout(request)  
    messages.success(request, "Vous avez été déconnecté.")
    return redirect('home')  


# Vue de profil (nécessite d'être connecté)
@login_required
def profile_view(request):
    user = request.user  
    return render(request, 'accueil/userprofil.html', {'user': user})

def find_view(request):
    jobs = Job.objects.all()  
    return render(request, 'accueil/find.html', {'jobs': jobs})



@login_required
def recruiter_profile_view(request):
    user = request.user  
    
    # Vérification du rôle de l'utilisateur
    if user.role != 'recruiter':  
        messages.error(request, "Vous n'avez pas l'autorisation d'accéder à cette page.")
        return redirect('profile')  

    return render(request, 'accueil/recruteurprofil.html', {'user': user})

@login_required
def post_job_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        company = request.POST.get('company')
        location = request.POST.get('location')
        salary_min = request.POST.get('salary_min')
        salary_max = request.POST.get('salary_max')
        job_type = request.POST.get('job_type')
        description = request.POST.get('description')

        if not company:
            messages.error(request, "Le nom de l'entreprise est requis.")
            return render(request, 'accueil/post_job.html')

        try:
            Job.objects.create(
                title=title,
                company=company,
                location=location,
                salary_min=salary_min,
                salary_max=salary_max,
                job_type=job_type,
                description=description
            )

            messages.success(request, "Offre d'emploi postée avec succès.")
            return redirect('find')  
        except Exception as e:
            messages.error(request, f"Une erreur s'est produite: {str(e)}")
            return render(request, 'accueil/post_job.html')

    return render(request, 'accueil/post_job.html')


def job_detail_view(request, job_id):
    
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'accueil/job_detail.html', {'job': job})

@login_required
def apply_job_view(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    user = request.user

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request, 'Votre candidature a été envoyée avec succès.')
            return redirect('find')
    else:
        form = ApplicationForm()

    return render(request, 'accueil/apply_job.html', {'job': job, 'form': form, 'user': user})


