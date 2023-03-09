from django.db import models
from users.models import User
import uuid

ROOM_TYPE_CHOICES = (("Shared", "Shared"), ("Single", "Single"), ("Double", "Double"), ("Triple", "Triple"))

class Accommodation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='accommodations/')
    rooms_number = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

class Room(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.CharField(max_length=255, choices=ROOM_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_from = models.DateField()
    available_to = models.DateField()
    description = models.TextField()
    photo = models.ImageField(upload_to='rooms/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    reservation_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)