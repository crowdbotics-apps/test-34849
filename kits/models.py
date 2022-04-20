from django.conf import settings
from django.db import models


class KitSleeve(models.Model):
    "Generated Model"
    kit_sleeve_id = models.UUIDField()
    sku = models.ForeignKey(
        "kits.Sku",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="kitsleeve_sku",
    )


class ActivationCard(models.Model):
    "Generated Model"
    activation_id = models.UUIDField()
    kit = models.ForeignKey(
        "kits.KitSleeve",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="activationcard_kit",
    )


class Sku(models.Model):
    "Generated Model"
    sku = models.CharField(
        max_length=32,
    )
    partner = models.ForeignKey(
        "partners.Partner",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="sku_partner",
    )


class CollectionDevice(models.Model):
    "Generated Model"
    device_id = models.UUIDField()
    kit = models.ForeignKey(
        "kits.KitSleeve",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="collectiondevice_kit",
    )


# Create your models here.
