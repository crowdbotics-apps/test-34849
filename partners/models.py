from django.conf import settings
from django.db import models


class Partner(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=64,
    )


# Create your models here.
