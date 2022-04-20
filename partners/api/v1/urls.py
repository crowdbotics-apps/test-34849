from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PartnerViewSet

router = DefaultRouter()
router.register("partner", PartnerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
