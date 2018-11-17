from datetime import datetime

from django import forms
from django.conf import settings


class LoadHours(forms.Form):
    CHOICES = [(i, str(i)) for i in range(1, settings.WORK_DAY_HOURS + 1)]
    hours = forms.ChoiceField(choices=CHOICES, label='Horas')
    date = forms.DateField(initial=datetime.today(), label='Fecha')
