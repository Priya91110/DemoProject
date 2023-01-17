from django.db import models

# Create your models here.
class NewProduct(models.Model):
    Name = models.CharField(max_length =50)
    Description = models.TextField(max_length = 225)
    Price = models.DecimalField( max_digits=5, decimal_places=2)
