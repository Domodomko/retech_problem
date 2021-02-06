from django.db import models

# Create your models here.


class Vending(models.Model):
    address = models.CharField(max_length=30, unique=True)
    count = models.PositiveIntegerField(default=0)
    max_size = models.PositiveIntegerField(default=0)
    id_key = models.CharField(max_length=30, unique=True)
    total_sum = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Vending'
        ordering = ['-total_sum']

    def __str__(self):
        return self.address