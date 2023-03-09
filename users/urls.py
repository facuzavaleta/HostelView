from django.urls import path, include
from .views import register, home_view

app_name="users"

urlpatterns = [
    path("auth/", include("django.contrib.auth.urls")),
    path('register/', register, name='register'),
    path('<str:user_type>/<str:username>/', home_view, name='home'),
]