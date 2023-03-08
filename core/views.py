from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home_view(request):
    return render(request, 'core/home.html')

def contact_view(request):
    return render(request, 'core/contact.html')

def about_view(request):
    return render(request, 'core/about.html')

def logout_view(request):
    logout(request)
    return redirect('core:home')