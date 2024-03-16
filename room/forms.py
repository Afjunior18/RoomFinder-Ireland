from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_image','room_description', 'owner_phone', 'room_type', 'room_location', 'price']
