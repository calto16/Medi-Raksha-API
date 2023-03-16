from django.db import models

# Create your models here.

class Medicine(models.Model):
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    therauptic_category = models.CharField(max_length=200)
    disease = models.CharField(max_length=200)
    description = models.TextField(max_length=500, null=True, blank=True)