from django.urls import path
from .views import signup_view, login_view, home_view, logout_view

urlpatterns = [
    path('home/', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),  # Agrega esta línea para la URL de logout
]