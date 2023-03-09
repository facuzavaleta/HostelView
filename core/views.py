from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from users.models import User
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'core/home.html')

def contact_view(request):
    return render(request, 'core/contact.html')

def about_view(request):
    return render(request, 'core/about.html')

def logout_view(request):
    logout(request)
    return redirect('core:home')

@login_required
def landpageredirect_view(request):
    username = request.user.username
    if request.user.user_type == 'Client':
        return redirect(f'/users/client/{username}')
    elif request.user.user_type == 'Admin':
        return redirect(f'/users/admin/{username}')