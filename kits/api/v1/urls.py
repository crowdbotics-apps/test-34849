from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ActivationCardViewSet,
    CollectionDeviceViewSet,
    KitSleeveViewSet,
    SkuViewSet,
)

router = DefaultRouter()
router.register("kitsleeve", KitSleeveViewSet)
router.register("activationcard", ActivationCardViewSet)
router.register("sku", SkuViewSet)
router.register("collectiondevice", CollectionDeviceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
