from django.contrib import admin
from .models import ActivationCard, CollectionDevice, KitSleeve, Sku

admin.site.register(KitSleeve)
admin.site.register(ActivationCard)
admin.site.register(Sku)
admin.site.register(CollectionDevice)

# Register your models here.
