from django.shortcuts import render
from django.http import HttpResponse

def HomePage(request):
    return render(request, 'home.html')
