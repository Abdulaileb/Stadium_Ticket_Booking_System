from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import BaseUserManager

class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group, blank=True, related_name='admin_users')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='admin_users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return self.email
    

class User(AbstractUser):
    full_name = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    user_email = models.EmailField(unique=True)
    date_of_birth = models.DateTimeField()
    groups = models.ManyToManyField(Group, blank=True, related_name='users')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='users')

    USERNAME_FIELD = 'user_email'

    def __str__(self):
        return self.user_email

