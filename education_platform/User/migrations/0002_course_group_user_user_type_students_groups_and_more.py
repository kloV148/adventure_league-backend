# Generated by Django 4.2.5 on 2023-10-16 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Edu', '0005_alter_homework_submission_student'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('Student', 'Student'), ('Courator', 'Courator'), ('Teacher', 'Teacher'), ('Comission', 'Comission'), ('Admin', 'Admin')], max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Students_Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.group')),
                ('student', models.ForeignKey(limit_choices_to={'user_type': 'Student'}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boss_first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('boss_second_name', models.CharField(blank=True, max_length=20, null=True)),
                ('boss_patronymic', models.CharField(blank=True, max_length=20, null=True)),
                ('department_name', models.CharField(blank=True, max_length=50, null=True)),
                ('working_position', models.CharField(blank=True, max_length=100, null=True)),
                ('experience', models.TextField(blank=True, max_length=300, null=True)),
                ('achievements', models.TextField(blank=True, max_length=500, null=True)),
                ('motivational_letter', models.TextField(blank=True, max_length=800, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Edu.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='courator',
            field=models.ForeignKey(limit_choices_to={'user_type': 'Courator'}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Edu.course'),
        ),
    ]
