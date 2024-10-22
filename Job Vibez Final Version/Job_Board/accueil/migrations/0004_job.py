# Generated by Django 5.1.1 on 2024-10-20 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0003_delete_persouser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('salary_min', models.DecimalField(decimal_places=2, max_digits=10)),
                ('salary_max', models.DecimalField(decimal_places=2, max_digits=10)),
                ('job_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]