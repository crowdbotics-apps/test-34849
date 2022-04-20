from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ActivationCardViewSet,
    CollectionDeviceViewSet,
    CollectionDeviceTypeViewSet,
    CollectionDeviceTypeSkusViewSet,
    KitSleeveViewSet,
    SkuViewSet,
)

router = DefaultRouter()
router.register("kitsleeve", KitSleeveViewSet)
router.register("activationcard", ActivationCardViewSet)
router.register("sku", SkuViewSet)
router.register("collectiondevice", CollectionDeviceViewSet)
router.register("collectiondevicetypeskus", CollectionDeviceTypeSkusViewSet)
router.register("collectiondevicetype", CollectionDeviceTypeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
