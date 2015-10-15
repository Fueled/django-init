# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Standard Library
import uuid

# Third Party Stuff
from django.db import migrations, models

# {{ cookiecutter.project_name }} Stuff
import {{cookiecutter.main_module}}.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('id', models.UUIDField(serialize=False, editable=False, default=uuid.uuid4, primary_key=True)),
                ('first_name', models.CharField(verbose_name='First Name', blank=True, max_length=120)),
                ('last_name', models.CharField(verbose_name='Last Name', blank=True, max_length=120)),
                ('email', models.EmailField(db_index=True, verbose_name='email address', unique=True, max_length=254)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('groups', models.ManyToManyField(related_name='user_set', verbose_name='groups', blank=True, related_query_name='user', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', verbose_name='user permissions', blank=True, related_query_name='user', to='auth.Permission', help_text='Specific permissions for this user.')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ('-date_joined',),
            },
            managers=[
                ('objects', {{cookiecutter.main_module}}.users.models.UserManager()),
            ],
        ),
    ]
