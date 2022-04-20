from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CarrierViewSet, SpeedViewSet

router = DefaultRouter()
router.register("speed", SpeedViewSet)
router.register("carrier", CarrierViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
