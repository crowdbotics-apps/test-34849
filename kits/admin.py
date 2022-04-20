from django.contrib import admin
from .models import (
    ActivationCard,
    CollectionDevice,
    CollectionDeviceType,
    CollectionDeviceTypeSkus,
    KitSleeve,
    Sku,
)

admin.site.register(KitSleeve)
admin.site.register(ActivationCard)
admin.site.register(Sku)
admin.site.register(CollectionDevice)
admin.site.register(CollectionDeviceTypeSkus)
admin.site.register(CollectionDeviceType)

# Register your models here.
