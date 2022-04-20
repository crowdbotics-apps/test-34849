from rest_framework import authentication
from kits.models import (
    ActivationCard,
    CollectionDevice,
    CollectionDeviceType,
    CollectionDeviceTypeSkus,
    KitSleeve,
    Sku,
)
from .serializers import (
    ActivationCardSerializer,
    CollectionDeviceSerializer,
    CollectionDeviceTypeSerializer,
    CollectionDeviceTypeSkusSerializer,
    KitSleeveSerializer,
    SkuSerializer,
)
from rest_framework import viewsets


class KitSleeveViewSet(viewsets.ModelViewSet):
    serializer_class = KitSleeveSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = KitSleeve.objects.all()


class ActivationCardViewSet(viewsets.ModelViewSet):
    serializer_class = ActivationCardSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ActivationCard.objects.all()


class SkuViewSet(viewsets.ModelViewSet):
    serializer_class = SkuSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Sku.objects.all()


class CollectionDeviceViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionDeviceSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CollectionDevice.objects.all()


class CollectionDeviceTypeSkusViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionDeviceTypeSkusSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CollectionDeviceTypeSkus.objects.all()


class CollectionDeviceTypeViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionDeviceTypeSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CollectionDeviceType.objects.all()
