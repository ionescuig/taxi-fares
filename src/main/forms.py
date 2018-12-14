from django import forms
from datetime import datetime

from .models import Journey


class JourneyForm(forms.ModelForm):
    date    = forms.DateField(label='Date',
                              required=True,
                              widget=forms.SelectDateWidget(),
                              initial=datetime.now)
    hour    = forms.TimeField(label='Hour',required=True,
                              widget=forms.TimeInput(format='%H:%M'),
                              initial=datetime.now().strftime('%H:%M'))
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
                                 required=True,
                                 min_value=0,
                                 initial=0)

    class Meta:
        model = Journey
        fields = [
            'date',
            'hour',
            'people',
            'miles',
            'toll',
        ]

    def __init__(self, *args, **kwargs):
        super(JourneyForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'class': 'form-control'})
        self.fields['hour'].widget.attrs.update({'class': 'form-control'})
        self.fields['people'].widget.attrs.update({'class': 'form-control'})
        self.fields['miles'].widget.attrs.update({'class': 'form-control'})
        self.fields['toll'].widget.attrs.update({'class': 'form-control'})


