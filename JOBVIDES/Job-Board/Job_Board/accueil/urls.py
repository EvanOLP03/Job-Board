from django.urls import path
from .views import home, student_signup, login_view, profile_view

urlpatterns = [
    path('', home, name='home'),  
    path('inscription/', student_signup, name='student_signup'), 
    path('login/', login_view, name='login'),  # Connexion sous /login/
    path('accounts/login/', login_view, name='login'),  # Optionnel : redirection vers login
    path('profile/', profile_view, name='profile'),
]
