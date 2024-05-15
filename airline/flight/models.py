from django.db import models
from django.db import models


# Create your models here.
class Flight(models.Model):
    FirstName = models.CharField(max_length=15)
    LastName = models.CharField(max_length=15)

    