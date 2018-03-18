from django.contrib import admin
from .models import Location, Resident, Stay

admin.site.register(Location)
admin.site.register(Resident)
admin.site.register(Stay)
