from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime
from django.db import models

USER_TYPE_CHOICES = (("Client", "Client"), ("Admin", "Admin"))

class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length = 255)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    created_on = models.DateTimeField(default=datetime.now)    
    USERNAME_FIELD = 'username'