from django.urls import path, include
from .views import accommodation_create

app_name="acommodations"

urlpatterns = [
    path('create/', accommodation_create, name='accommodation_create'),
]