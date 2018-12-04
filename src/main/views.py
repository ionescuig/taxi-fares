from django.views.generic import CreateView, UpdateView

from .calculator import check_tariff
from .forms import JourneyForm
from .models import BankHoliday, Tariff, Journey


class HomeCreateView(CreateView):
    template_name = 'main/index.html'
    form_class = JourneyForm


class HomeUpdateView(UpdateView):
    template_name = 'main/index.html'
    form_class = JourneyForm

    def get_queryset(self):
        try:
            return Journey.objects.filter(name='quote')
        except:
            pass

    def get_context_data(self, *args, **kwargs):
        context = super(HomeUpdateView, self).get_context_data(*args, **kwargs)
        date = self.get_object().date
        hour = self.get_object().hour
        miles = self.get_object().miles
        no_of_people = self.get_object().people
        toll = self.get_object().toll

        bank_holidays = BankHoliday.objects.all()
        bank_holiday = False

        for item in bank_holidays:
            if date == item.date:
                bank_holiday = True

        tariff_fare = check_tariff(date, hour, bank_holiday)
        print(tariff_fare)

        # check_tariff(date, hour, bank_holiday):
        #   - not working for 4/12/2018 22:51
        #   - not working for bank holiday midnight to morning
        #   - check all

        return context
