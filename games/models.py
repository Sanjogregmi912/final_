from django.db import models

# Create your models here.
class Games(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    image=models.FileField(upload_to='games', default="defaul.jpg")

    class Meta:
        db_table="games"


