from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ActivationCardViewSet, KitSleeveViewSet, SkuViewSet

router = DefaultRouter()
router.register("kitsleeve", KitSleeveViewSet)
router.register("activationcard", ActivationCardViewSet)
router.register("sku", SkuViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
