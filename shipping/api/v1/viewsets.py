from rest_framework import authentication
from shipping.models import Carrier, Speed, TrackingNumber, Type
from .serializers import (
    CarrierSerializer,
    SpeedSerializer,
    TrackingNumberSerializer,
    TypeSerializer,
)
from rest_framework import viewsets


class SpeedViewSet(viewsets.ModelViewSet):
    serializer_class = SpeedSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Speed.objects.all()


class CarrierViewSet(viewsets.ModelViewSet):
    serializer_class = CarrierSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Carrier.objects.all()


class TrackingNumberViewSet(viewsets.ModelViewSet):
    serializer_class = TrackingNumberSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TrackingNumber.objects.all()


class TypeViewSet(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Type.objects.all()
