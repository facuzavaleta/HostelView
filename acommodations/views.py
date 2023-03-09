from django.shortcuts import render, redirect
from .forms import AccommodationForm
# Create your views here.
def accommodation_create(request, user_type, username):
    if request.method == 'POST':
        form = AccommodationForm(request.POST)
        if form.is_valid():
            accommodation = form.save(commit=False)
            accommodation.user = request.user  # Agrega el usuario actual como creador del objeto
            accommodation.save()
            return render(request, 'accommodation_create_success.html')  # Redirige a la página principal
    else:
        form = AccommodationForm()
    context = {
        'user_type': user_type,
        'username': username,
        'form': form,
    }
    return render(request, 'accommodation_create.html', context)