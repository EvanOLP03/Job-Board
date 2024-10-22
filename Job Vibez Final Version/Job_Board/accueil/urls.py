from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inscription/', views.student_signup, name='student_signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('find/', views.find_view, name='find'),
    path('recruiter_profile/', views.recruiter_profile_view, name='recruiter_profile'),
    path('post_job/', views.post_job_view, name='post_job'),
    path('job/<int:job_id>/', views.job_detail_view, name='job_detail'),
    path('apply/<int:job_id>/', views.apply_job_view, name='apply_job'),

       
]
