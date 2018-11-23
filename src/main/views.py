from django.shortcuts import render
from .models import BankHoliday, Tariff


def index(request):
    return render(request, 'main/index.html')
