from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CarrierViewSet, SpeedViewSet, TrackingNumberViewSet, TypeViewSet

router = DefaultRouter()
router.register("speed", SpeedViewSet)
router.register("carrier", CarrierViewSet)
router.register("trackingnumber", TrackingNumberViewSet)
router.register("type", TypeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
