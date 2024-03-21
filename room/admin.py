from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Room
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class PriceRangeFilter(admin.SimpleListFilter):
    """
    Added PriceRangeFilter class to enable filtering rooms
    by price range in admin panel.
    """
    title = "Price Range"
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return (
            ('1', _('Less than $500')),
            ('2', _('$500 - $1000')),
            ('3', _('$1000 - $1500')),
            ('4', _('More than $1500')),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter(price__lt=500)
        elif self.value() == '2':
            return queryset.filter(price__range=[500, 1000])
        elif self.value() == '3':
            return queryset.filter(price__range=[1000, 1500])
        elif self.value() == '4':
            return queryset.filter(price__gt=1500)


@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Room model.
    """

    list_display = (
                    'room_description', 'room_owner', 'room_availability',
                    'room_type', 'owner_email', 'owner_phone', 'room_location',
                    'price', 'created_on', 'is_pending_approval'
                    )
    search_fields = [
                    'room_description', 'room_location'
                    ]
    list_filter = (
                     'created_on', 'room_type',
                     'is_pending_approval', PriceRangeFilter
                    )
    actions = [
                'approve_rooms'
                ]
    summernote_fields = (
                        'room_description'
                        )

    def approve_rooms(self, request, queryset):
        queryset.update(is_pending_approval=False)

    approve_rooms.short_description = ("Approve selected rooms")