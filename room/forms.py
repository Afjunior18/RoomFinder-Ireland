from django import forms
from django.core.exceptions import ValidationError
from .models import Room

class RoomForm(forms.ModelForm):
    # Validate owner's phone number format
    def clean_owner_phone(self):
        owner_phone = self.cleaned_data.get('owner_phone')
        if not owner_phone.startswith('+') or not owner_phone[1:].isdigit():
            raise forms.ValidationError("Phone number must start with '+' and contain only digits.")
        return owner_phone

    class Meta:
        model = Room
        fields = ['room_image','room_description', 'owner_phone','owner_email', 'room_type', 'room_location', 'price']
