from django.shortcuts import render

# Create your views here.
def client_login(request):
    return render(request, 'users/client_login.html')

def admin_login(request):
    return render(request, 'users/admin_login.html')

def register(request):
    return render(request, 'users/register.html')