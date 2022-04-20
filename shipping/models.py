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
        on_delete=models.CASCADE,
        null=True,
        blank=True,
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


# Create your models here.
