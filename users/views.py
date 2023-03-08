from django.shortcuts import render

# Create your views here.
def client_login(request):
    return render(request, 'users/client_login.html')

def client_register(request):
    return render(request, 'users/client_register.html')

def admin_login(request):
    return render(request, 'users/admin_login.html')

def admin_register(request):
    return render(request, 'users/admin_register.html')