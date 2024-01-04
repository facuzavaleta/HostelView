from django.contrib import admin
from django.urls import path, include
from pages.views import landing_view

urlpatterns = [
    path('', landing_view, name='landing'),
]
