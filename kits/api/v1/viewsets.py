from rest_framework import authentication
from kits.models import ActivationCard, KitSleeve, Sku
from .serializers import ActivationCardSerializer, KitSleeveSerializer, SkuSerializer
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
