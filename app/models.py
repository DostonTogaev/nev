from django.db import models

# Create your models here.
class Product(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5
    name = models.CharField(max_length=255, null=True,blank=True)
    descirtion = models.CharField(max_length=250, null=True, blank=True)
    price = models.FloatField()
    discount =models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')

    created_at =models.DateTimeField(auto_created=True)
    upload_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def discount_priced(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

class Customers(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email= models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField()
    addres = models.CharField(max_length=255, null=True, blank=True)
    Joined = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f'{self.name}'
