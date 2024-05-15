from django.db import models
from django.db import models


# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64, blank=False, null=True)
    destination = models.CharField(max_length=55)
    origin = models.IntegerField()
    FirstName = models.CharField(max_length=15, blank=False, null=True)
    LastName = models.CharField(max_length=15, blank=False, null=True)

    class Meta:
        db_table = "Flight"