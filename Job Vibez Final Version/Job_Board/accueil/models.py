from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings

class People(models.Model):
    ROLE_CHOICES = [
        ('recruiter', 'Recruiter'),
        ('applicant', 'Applicant'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='applicant')
    company_id = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    @property
    def is_authenticated(self):
        return True  

    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False  

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    
class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2)
    job_type = models.CharField(max_length=100)  
    description = models.TextField()

    def __str__(self):
        return self.title

    
class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    contact_email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Application(models.Model):
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    cover_letter_file = models.FileField(upload_to='cover_letters/', blank=True, null=True)  
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Candidature de {self.applicant} pour {self.job}"

