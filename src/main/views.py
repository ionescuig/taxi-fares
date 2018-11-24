from django.shortcuts import render
from django.views.generic import CreateView
from .forms import JourneyForm
from .models import BankHoliday, Tariff


def index(request):
    return render(request, 'main/index.html')


def check(request):
    form = JourneyForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            return render(request, 'main/index.html', {'form': form})
    else:
        form = JourneyForm()

    return render(request, 'main/index.html', {'form': form})
