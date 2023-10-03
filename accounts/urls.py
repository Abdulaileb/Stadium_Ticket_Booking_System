from django.urls import path

from django.contrib.auth import views as auth_views
from .views import *

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.user_registration, name='userSignUp'),
]