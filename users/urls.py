from django.urls import path
from .views import client_login, admin_login, client_register, admin_register

app_name="users"

urlpatterns = [
    path('client/login', client_login, name='client_login'),
    path('client/register', client_register, name='client_register'),
    path('admin/login', admin_login, name='admin_login'),
    path('admin/register', admin_register, name='admin_register'),
]
