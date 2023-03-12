from django.urls import path, include
from .views import register, client_landpage_view, admin_landpage_view

app_name="users"

urlpatterns = [
    path("auth/", include("django.contrib.auth.urls")),
    path('register/', register, name='register'),
    path('client/<str:username>/', client_landpage_view, name='client_landpage_view'),
    path('client/<str:username>/accommodations/', include('acommodations.urls')),
    path('admin/<str:username>/', admin_landpage_view, name='admin_landpage_view'),
    path('admin/<str:username>/accommodations/', include('acommodations.urls')),
]