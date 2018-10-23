from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import SelectDateWidget

from apps.tracking.models import Employee, Project, Task


class LoadHours(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())
    task = forms.ModelChoiceField(queryset=None)

    hours = forms.IntegerField()
    date = forms.DateField()

    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project')
        super().__init__(*args, **kwargs)
        self.fields['task'].queryset = Task.objects.filter(project=project)
