from django.urls import path
from .views import home, student_signup, login_view  

urlpatterns = [
    path('', home, name='home'),  
    path('inscription/', student_signup, name='student_signup'), 
    path('login/', login_view, name='login'),
]
