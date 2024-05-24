from django.db import models
from django.db import models


# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64, blank=False, null=True)
    destination = models.CharField(max_length=55, blank=False, null=True)
    FirstName = models.CharField(max_length=15, blank=False, null=True)
    LastName = models.CharField(max_length=15, blank=False, null=True)

    def __str__(self):
        return f"{self.FirstName}: {self.LastName}: {self.origin} to {self.destination}"
    
    def insertuser(self):
        return self.origin != self.destination

    class Meta:
        db_table = "Flight"

class passenger(models.Model):
    FirstName = models.CharField(max_length=15, blank=False, null=True)
    LastName = models.CharField(max_length=15, blank=False, null=True)

    