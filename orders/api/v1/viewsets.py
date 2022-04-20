from rest_framework import authentication
from orders.models import LineItem, Order, OrderSystem
from .serializers import LineItemSerializer, OrderSerializer, OrderSystemSerializer
from rest_framework import viewsets


class LineItemViewSet(viewsets.ModelViewSet):
    serializer_class = LineItemSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = LineItem.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Order.objects.all()


class OrderSystemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSystemSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = OrderSystem.objects.all()
