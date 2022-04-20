from rest_framework import authentication
from shipping.models import Carrier, Speed
from .serializers import CarrierSerializer, SpeedSerializer
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
