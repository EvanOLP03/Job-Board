from django.db import models

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

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
