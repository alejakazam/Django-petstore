from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=30)
    description= models.CharField(max_length=200)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='products/')
    stock= models.IntegerField()
    def __str__(self):
        return self.name

