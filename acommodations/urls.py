from django.urls import path, include
from .views import accommodation_create, accommodations_listall

app_name="acommodations"

urlpatterns = [
    path('create/', accommodation_create, name='accommodation_create'),
    path('listall/', accommodations_listall, name='acoommodations_listall'),
]