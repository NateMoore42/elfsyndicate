# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 10:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name=b'username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name=b'email address')),
                ('is_staff', models.BooleanField(default=False, verbose_name=b'staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date joined')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.TextField(blank=True, max_length=500, verbose_name=b'profile description')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name=b'first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name=b'last name')),
                ('gender', models.CharField(blank=True, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other')], max_length=1, null=True, verbose_name=b'gender')),
                ('profile_picture', models.ImageField(blank=True, upload_to=b'profile-pictures/%Y/%m/%d')),
                ('dob', models.DateField(blank=True, null=True, verbose_name=b'birthday')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
