# Generated by Django 5.2.4 on 2025-07-19 04:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employer_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('candidate_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_education', models.CharField(max_length=100, null=True)),
                ('work_experience', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('Interview', 'Interview'), ('Offered', 'Offered'), ('Rejected', 'Rejected')], max_length=20, null=True)),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='candidate_app.candidateprofilemodel')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employer_app.jobmodel')),
            ],
        ),
    ]
