from django.contrib import admin
from .models import People, Job
from django.contrib.auth.models import User, Group


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'salary_min', 'salary_max', 'job_type')
    search_fields = ('title', 'company', 'location')

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(People)