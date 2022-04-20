from django.conf import settings
from django.db import models


class Speed(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=64,
    )
    speed_days = models.IntegerField()
    carrier = models.ForeignKey(
        "shipping.Carrier",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="speed_carrier",
    )


class Carrier(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=64,
    )
    scac = models.CharField(
        max_length=6,
    )


class TrackingNumber(models.Model):
    "Generated Model"
    tracking_number = models.CharField(
        max_length=128,
    )
    shipping_speed = models.ForeignKey(
        "shipping.Speed",
        on_delete=models.CASCADE,
        related_name="trackingnumber_shipping_speed",
    )
    kit_sleeve = models.ForeignKey(
        "kits.KitSleeve",
        on_delete=models.CASCADE,
        related_name="trackingnumber_kit_sleeve",
    )
    type = models.ForeignKey(
        "shipping.Type",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="trackingnumber_type",
    )
    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="trackingnumber_order",
    )


class Type(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=32,
    )


# Create your models here.
