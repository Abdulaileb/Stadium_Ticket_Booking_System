from django import forms
from django.contrib.auth import get_user_model

from django import forms
from .models import AdminUser, User

class AdminUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = ['username', 'email', 'full_name', 'designation', 'password']

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'full_name', 'city', 'gender', 'user_email', 'date_of_birth', 'password']
