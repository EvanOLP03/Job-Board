# Generated by Django 5.1.1 on 2024-10-17 22:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='password',
            field=models.CharField(default=2, max_length=128),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='PersoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('diplomas', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('cover_letter', models.TextField(blank=True, null=True)),
                ('people', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accueil.people')),
            ],
        ),
    ]
