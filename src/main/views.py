from django.views.generic import CreateView, UpdateView

from .forms import JourneyForm
from .models import BankHoliday, Tariff, Journey


class HomeCreateView(CreateView):
    template_name = 'main/index.html'
    form_class = JourneyForm


class HomeUpdateView(UpdateView):
    template_name = 'main/index.html'
    form_class = JourneyForm

    def get_queryset(self):
        # obj = Journey.objects.filter(name='quote')
        try:
            # return Journey.objects.filter(pk=obj[0].pk)
            return Journey.objects.filter(name='quote')
        except:
            pass

    # def get_context_data(self, *args, **kwargs):
    #     context = super(HomeUpdateView, self).get_context_data(*args, **kwargs)
    #     return context

    # def get_form_kwargs(self):
    #     kwargs = super(HomeUpdateView, self).get_form_kwargs()
    #     print(kwargs)
    #     return kwargs
