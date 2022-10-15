from django.db import models


class RetailShop(models.Model):
    title = models.CharField(max_length=150)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title
