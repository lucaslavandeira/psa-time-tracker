from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import SelectDateWidget

from apps.tracking.models import Employee, Project, Task


class LoadHours(forms.Form):
    CHOICES = ((1, '1'),
               (2, '2'),
               (3, '3'),
               (5, '5'),
               (8, '8'),
               )
    hours = forms.ChoiceField(choices=CHOICES, label="", help_text="")
