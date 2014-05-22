from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __unicode__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    giftwrap = models.BooleanField(default=False)
    products = models.ManyToManyField(Product)

    def __unicode__(self):
        return self.name