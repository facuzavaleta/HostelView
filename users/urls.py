from django.urls import path
from .views import client_login, admin_login, register

app_name="users"

urlpatterns = [
    path('client/login', client_login, name='client_login'),
    path('admin/login', admin_login, name='admin_login'),
    path('register', register, name='register'),
]
