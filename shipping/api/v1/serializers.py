from rest_framework import serializers
from shipping.models import Carrier, Speed


class SpeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speed
        fields = "__all__"


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = "__all__"
