# Generated by Django 5.2.4 on 2025-07-19 04:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('about_company', models.TextField(null=True)),
                ('company_logo', models.ImageField(upload_to='media/company-logo')),
                ('location', models.CharField(max_length=100, null=True)),
                ('employer_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('requirements', models.TextField(null=True)),
                ('sallary', models.PositiveIntegerField(null=True)),
                ('job_type', models.CharField(choices=[('Full_time', 'Full_time'), ('Remote', 'Remote'), ('Internship', 'Internship')], max_length=20, null=True)),
                ('deadline', models.DateField(null=True)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('employer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employer_app.employerprofilemodel')),
            ],
        ),
    ]
