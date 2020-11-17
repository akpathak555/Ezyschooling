from django.db import models
# Create your models here.


class Pizza(models.Model):
    pizza_name = models.CharField('Name', max_length=255, null=True, blank=True)
    pizza_size = models.CharField('Size', max_length=255, null=True, blank=True)
    pizza_type = models.CharField('Type', max_length=255, null=True, blank=True)
    pizza_price = models.IntegerField('Price', null=True, blank=True)

    def __str__(self):
        return str(self.pizza_name)