from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import AdminUserRegistrationForm, UserRegistrationForm

def admin_user_registration(request):
    if request.method == 'POST':
        form = AdminUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('admin:index')  # Redirect to admin dashboard or any other page
    else:
        form = AdminUserRegistrationForm()
    return render(request, 'registration/admin_user_registration.html', {'form': form})

def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_dashboard')  # Redirect to student dashboard or any other page
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/user_registration.html', {'form': form})
