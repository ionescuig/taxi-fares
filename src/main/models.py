from django.core.urlresolvers import reverse
from django.db import models
import datetime
from django.utils import timezone


class Tariff(models.Model):
    name        = models.CharField(max_length=20)
    description = models.TextField(default='')
    start       = models.DecimalField(max_digits=5, decimal_places=2)
    start_label = models.CharField(max_length=100,
                                   default='For any distance up to one tenth of a mile')
    first       = models.DecimalField(max_digits=5, decimal_places=2)
    first_label = models.CharField(max_length=100,
                                   default='The next one tenth of a mile')
    second      = models.DecimalField(max_digits=5, decimal_places=2)
    second_label = models.CharField(max_length=100,
                                    default='For each subsequent one fifth of a mile')
    waiting     = models.DecimalField(max_digits=5, decimal_places=2)
    waiting_label = models.CharField(max_length=100,
                                     default='Each completed period of 60 seconds waiting time')

    def __str__(self):
        return self.name

    def get_description(self):
        return self.description.split(",")


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
