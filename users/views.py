from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.urls import reverse
from .models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseNotFound
from acommodations.models import Accommodation

def is_client(user):
    return user.is_authenticated and user.user_type == 'Client'

def is_admin(user):
    return user.is_authenticated and user.user_type == 'Admin'
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
        
@user_passes_test(is_client)
def client_landpage_view(request, username):

    accommodations_all = Accommodation.objects.all()
    context = {
        'username': username,
        'accommodations_all': accommodations_all,
    }
    
    return render(request, 'users/client/clientlandpage.html', context)

@user_passes_test(is_admin)
def admin_landpage_view(request, username):
    accommodations_admin = Accommodation.objects.filter(user__id=request.user.id)

    context = {
        'username': username,
        'accommodations_admin': accommodations_admin,
    }
    
    return render(request, 'users/admin/adminlandpage.html', context)
