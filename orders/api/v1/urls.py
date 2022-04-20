from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import LineItemViewSet, OrderViewSet, OrderSystemViewSet

router = DefaultRouter()
router.register("lineitem", LineItemViewSet)
router.register("order", OrderViewSet)
router.register("ordersystem", OrderSystemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
