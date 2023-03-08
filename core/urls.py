from django.urls import path, include
from .views import home_view, about_view, contact_view, logout_view

app_name="core"

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('users/', include("users.urls")),
    path('logout/', logout_view, name='logout'),
]
