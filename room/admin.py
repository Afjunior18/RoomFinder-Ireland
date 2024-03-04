from django.contrib import admin
from .models import Room
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):

    list_display = ('room_description', 'room_owner', 'room_availability', 'room_type', 'owner_email', 'owner_phone', 'room_location', 'price', 'created_on', 'status')
    search_fields = ['room_description', 'room_location']
    list_filter = ('status', 'room_availability', 'room_type')
    summernote_fields = ('room_description', 'excerpt')

# Register your models here.

# admin.site.register(Room)