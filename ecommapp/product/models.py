from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(max_digits=100000, decimal_places=2)
    quantity = models.DecimalField(decimal_places=0,max_digits=10000) 