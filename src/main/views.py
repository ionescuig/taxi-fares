from django.views.generic import CreateView, UpdateView, TemplateView

from .calculator import check_tariff, calculate_fare
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

        selected_tariff = Tariff.objects.filter(name=tariff_fare)[0]
        fare = calculate_fare(
            [
                float(selected_tariff.start),
                float(selected_tariff.first),
                float(selected_tariff.second),
                float(selected_tariff.waiting)
            ],
            float(miles),
            float(no_of_people),
            float(toll)
        )

        # print('>>> Date: ', date,
        #       '\t Time: ', hour,
        #       '\t Miles: ', miles,
        #       '\t Passengers: ', no_of_people,
        #       '\t Toll: ', toll)
        # print('>>> Tariff: ', tariff_fare,
        #       '\t Fare: %.2f ' % fare)

        context['tariff'] = selected_tariff
        context['fare'] = fare

        return context


class FaresView(TemplateView):
    template_name = 'main/fares.html'
