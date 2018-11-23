from django.db import models


class Tariff(models.Model):
    name        = models.CharField(max_length=10)
    start       = models.DecimalField(max_digits=5, decimal_places=2)
    first       = models.DecimalField(max_digits=5, decimal_places=2)
    second      = models.DecimalField(max_digits=5, decimal_places=2)
    waitting    = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class BankHoliday(models.Model):
    date = models.DateField()

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')
