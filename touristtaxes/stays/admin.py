from django.contrib import admin

from .models import Location, Owner, Stay

admin.site.register(Location)
admin.site.register(Owner)
admin.site.register(Stay)
