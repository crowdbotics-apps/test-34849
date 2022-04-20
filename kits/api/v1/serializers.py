from rest_framework import serializers
from kits.models import ActivationCard, CollectionDevice, KitSleeve, Sku


class KitSleeveSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitSleeve
        fields = "__all__"


class ActivationCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivationCard
        fields = "__all__"


class SkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sku
        fields = "__all__"


class CollectionDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionDevice
        fields = "__all__"
