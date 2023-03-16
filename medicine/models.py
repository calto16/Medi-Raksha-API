from django.db import models

# Create your models here.

class Medicine(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    manufacturer = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.CharField(max_length=100, null=True, blank=True)
    dosage = models.CharField(max_length=100, null=True, blank=True)
    substance = models.CharField(max_length=100, null=True, blank=True)
    therauptic_category = models.CharField(max_length=200, blank=True, null=True)
    disease = models.CharField(max_length=200, blank=True, null=True)
    