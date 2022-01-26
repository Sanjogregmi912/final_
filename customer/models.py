from django.db import models

class Customer(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

class Meta:
    bd_table='customer'
