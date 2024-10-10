from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),  
    path('inscription/', views.student_signup, name='student_signup'),
    path('login/', views.login_view, name='login'),
]
