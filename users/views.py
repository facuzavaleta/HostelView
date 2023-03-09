from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("core:landpageredirect_view"))
        else:
            return render(request, "users/register_fail.html", {})
        
@login_required
def home_view(request, user_type):
    if user_type == 'client':
        return render(request, 'users/client/clientlandpage.html')
    elif user_type == 'admin':
        return render(request, 'users/admin/adminlandpage.html')