from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __unicode__(self):
        return self.name