from django.core.urlresolvers import reverse
from django.db import models
import datetime
from django.utils import timezone


class Tariff(models.Model):
    name    = models.CharField(max_length=10)
    start   = models.DecimalField(max_digits=5, decimal_places=2)
    first   = models.DecimalField(max_digits=5, decimal_places=2)
    second  = models.DecimalField(max_digits=5, decimal_places=2)
    waiting = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class BankHoliday(models.Model):
    date = models.DateField()

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')


class Journey(models.Model):
    name    = models.CharField(max_length=25, default='quote')
    date    = models.DateField()
    hour    = models.TimeField()
    people  = models.IntegerField()
    miles   = models.DecimalField(max_digits=5, decimal_places=2)
    toll    = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.date.strftime('%Y-%m-%d') + ', ' + self.hour.strftime('%H:%M')

    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})
