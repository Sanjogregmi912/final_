from django.db import models

from games.models import Games
from customer.models import Customer

# Create your models here.
class Booking(models.Model):
    booking_id=models.AutoField(auto_created=True,primary_key=True)
    game=models.ForeignKey(Games,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    date=models.CharField(max_length=50)
class Meta:
    db_table="booking"