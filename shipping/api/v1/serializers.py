from rest_framework import serializers
from shipping.models import Carrier, Speed, TrackingNumber, Type


class SpeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speed
        fields = "__all__"


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = "__all__"


class TrackingNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingNumber
        fields = "__all__"


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"
