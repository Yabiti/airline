from django.db import models
from django.db import models


# Create your models here.
class Flight(models.Model):
    Origin = models.CharField(max_length=64, blank=False, null=True)
    Destination = models.CharField(max_length=55, blank=False, null=True)
    FirstName = models.CharField(max_length=15, blank=False, null=True)
    LastName = models.CharField(max_length=15, blank=False, null=True)
# return strings
    def __str__(self):
        return f"{self.FirstName}: {self.LastName}: {self.Origin} to {self.Destination}"
# checking user inpuvalid or not    
    def insertuser(self):
        return self.Origin != self.Destination
# creating tabele using db
    class Meta:
        db_table = "Flight"