from django.db import models

# Create your models here.
#class to change to model
class Cloth(models.Model):
    
    name = models.CharField(max_length= 100)
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')