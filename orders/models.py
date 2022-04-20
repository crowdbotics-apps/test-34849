from django.conf import settings
from django.db import models


class LineItem(models.Model):
    "Generated Model"
    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.CASCADE,
        related_name="lineitem_order",
    )
    sku = models.ForeignKey(
        "kits.Sku",
        on_delete=models.CASCADE,
        related_name="lineitem_sku",
    )
    kit = models.ForeignKey(
        "kits.KitSleeve",
        on_delete=models.CASCADE,
        related_name="lineitem_kit",
    )


class Order(models.Model):
    "Generated Model"
    system = models.ForeignKey(
        "orders.OrderSystem",
        on_delete=models.CASCADE,
        related_name="order_system",
    )
    order_id = models.CharField(
        max_length=128,
    )
    order_time = models.DateTimeField()
    fulfillment_time = models.DateTimeField()
    cancelled_time = models.DateTimeField()


class OrderSystem(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=64,
    )


# Create your models here.
