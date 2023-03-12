from django.shortcuts import render, redirect
from .forms import AccommodationForm
from django.urls import reverse
from .models import Accommodation

# Create your views here.
def accommodation_create(request, user_type, username):
    if request.method == 'POST':
        form = AccommodationForm(request.POST)
        if form.is_valid():
            accommodation = form.save(commit=False)
            accommodation.user = request.user  # Agrega el usuario actual como creador del objeto
            accommodation.save()
            return redirect(reverse("core:landpageredirect_view"))
    else:
        form = AccommodationForm()

    context = {
        'user_type': user_type,
        'username': username,
        'form': form,
    }
    
    return render(request, 'accommodation_create.html', context)

def accommodations_listall(request, username):
    accommodations = Accommodation.objects.all()
    context = {
        'username': username,
        'accommodations': accommodations,
    }
    return render(request, 'accommodations_listall.html', context)