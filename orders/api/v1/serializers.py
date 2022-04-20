from rest_framework import serializers
from orders.models import LineItem, Order, OrderSystem


class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderSystem
        fields = "__all__"
