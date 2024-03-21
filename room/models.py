from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

from cloudinary.models import CloudinaryField


# Create your models here.

class Room(models.Model):
    """
    Model representing a room listing.

    Attributes:
        room_description (TextField): Description of the room.
        room_owner (ForeignKey): Owner of the room.
        room_availability (BooleanField): Indicates if the room is available.
        room_type (CharField): Type of the room (Single, Shared).
        owner_email (EmailField): Email of the owner.
        owner_phone (CharField): Phone number of the owner.
        room_image (CloudinaryField): Image of the room.
        room_location (CharField): Location of the room.
        price (DecimalField): Price of the room.
        created_on (DateTimeField): Date and time when the room was created.
        is_pending_approval (BooleanField): Indicates if the
        room is pending approval.
    """

    room_description = models.TextField()
    room_owner = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name="room_posts")
    room_availability = models.BooleanField(default=True)

    ROOM_TYPES = [
        ('S', 'Single'),
        ('SH', 'Shared'),
    ]
    room_type = models.CharField(max_length=2, choices=ROOM_TYPES)

    owner_email = models.EmailField(max_length=200)
    owner_phone = models.CharField(max_length=15,
                                   validators=[MinLengthValidator(10)])

    room_image = CloudinaryField('image', default='placeholder')

    room_location = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)

    is_pending_approval = models.BooleanField(default=True)

    class Meta:
        ordering = ["price"]

    def __str__(self):
        return (
            f"Available Room in: {self.room_location} "
            f"for only: $ {self.price}"
        )
