from django.contrib import admin
from .models import Carrier, Speed, TrackingNumber, Type

admin.site.register(Speed)
admin.site.register(Carrier)
admin.site.register(TrackingNumber)
admin.site.register(Type)

# Register your models here.
