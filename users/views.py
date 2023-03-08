from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.urls import reverse

# Create your views here.
def client_login(request):
    return render(request, 'users/client_login.html')

def admin_login(request):
    return render(request, 'users/admin_login.html')

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
            return redirect(reverse("core:home"))
        else:
            return render(request, "users/register_fail.html", {})