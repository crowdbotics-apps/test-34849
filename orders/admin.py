from django.contrib import admin
from .models import LineItem, Order, OrderSystem

admin.site.register(LineItem)
admin.site.register(Order)
admin.site.register(OrderSystem)

# Register your models here.
