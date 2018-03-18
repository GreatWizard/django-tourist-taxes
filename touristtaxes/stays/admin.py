from django.contrib import admin
from .models import Location, Resident, Stay


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ResidentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'location',
        'date_begin',
        'date_end',
    )


class StayAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'location',
        'date_begin',
        'date_end',
        'adults',
        'children',
        'is_validated'
    )


admin.site.register(Location, LocationAdmin)
admin.site.register(Resident, ResidentAdmin)
admin.site.register(Stay, StayAdmin)
