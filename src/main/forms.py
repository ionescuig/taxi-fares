from django import forms
from datetime import datetime
from .models import Journey


class JourneyForm(forms.Form):
    when    = forms.DateTimeField(label='Date',
                                  required=True,
                                  widget=forms.SplitDateTimeWidget(date_format='%d/%m/%Y', time_format='%H:%m'),
                                  initial=datetime.now)
    people  = forms.IntegerField(label='People',
                                 required=True,
                                 min_value=1,
                                 max_value=8,
                                 initial=1)
    miles   = forms.DecimalField(label='Miles',
                                 required=True,
                                 min_value=0,
                                 initial=0)
    toll    = forms.DecimalField(label='Toll',
                                 required=False,
                                 min_value=0,
                                 initial=0)

    class Meta:
        model = Journey
        fields = [
            'when',
            'people',
            'miles',
            'toll',
        ]

    def __init__(self, *args, **kwargs):
        super(JourneyForm, self).__init__(*args, **kwargs)
        self.fields['when'].widget.attrs.update({'class': 'form-control'})
        self.fields['people'].widget.attrs.update({'class': 'form-control'})
        self.fields['miles'].widget.attrs.update({'class': 'form-control'})
        self.fields['toll'].widget.attrs.update({'class': 'form-control'})


