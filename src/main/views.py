from django.shortcuts import render
from django.views.generic import ListView
from .models import BankHoliday, Tariff


def index(request):
    return render(request, 'main/index.html')