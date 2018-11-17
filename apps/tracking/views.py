from django.urls import reverse
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from apps.tracking.forms import LoadHours
from .models import Project, Employee, Task


def landing(request):
    employee = Employee.get_from_session()
    context = {
        'projects': employee.assigned_projects.all(),
    }

    return render(request, 'landing.html', context)


def project_detail(request, project):
    project = Project.objects.get(id=project)
    employee = Employee.get_from_session()
    context = {
        'project': project,
        'form': LoadHours(auto_id=False),
        'employee': employee,
    }

    return render(request, 'project_detail.html', context)


class TaskView(View):
    def getcontext(self, project, task):
        return {
            'form': LoadHours(),
            'project': Project.objects.get(id=project),
            'task': Task.objects.get(id=task),
        }

    def get(self, request, project, task):
        context = self.getcontext(project, task)
        return render(request, 'load_hours.html', context)

    def post(self, request, project, task):
        task_model = Task.objects.get(id=task)
        form = LoadHours(request.POST)
        employee = Employee.get_from_session()
        if form.is_valid():
            try:
                employee.spend_hours(task_model, int(form.cleaned_data['hours']), form.cleaned_data['date'])
            except ValueError as e:
                context = self.getcontext(project, task)
                context["error"] = e
                return render(request, 'load_hours.html', context=context)

            return HttpResponseRedirect(reverse('project-detail', kwargs={'project': project}))

        return HttpResponse("rompiste todo")
