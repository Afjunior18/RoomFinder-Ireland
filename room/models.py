from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

# Create your models here.

class Room(models.Model):
    room_description = models.TextField()
    room_owner = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="room_posts")
    room_availability = models.BooleanField(default=True)
    
    ROOM_TYPES = [
        ('S', 'Single'),  
        ('SH', 'Shared'),
    ]
    room_type = models.CharField(max_length=2, choices=ROOM_TYPES)

    room_photos = CloudinaryField('image')
    room_location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
