from django.views import View
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render

from apps.tracking.forms import LoadHours
from .models import Project


def hello(request):
    context = {
        'projects': Project.objects.all()
    }

    return render(request, 'tracker.html', context)


class ProjectDetail(View):
    def get(self, request, project):
        project = Project.objects.get(id=project)
        context = {
            'project': project,
            'form': LoadHours(project=project),
        }

        return render(request, 'project_detail.html', context)

    def post(self, request, project):
        project = Project.objects.get(id=project)

        form = LoadHours(request.POST, project=project)

        if form.is_valid():
            task = form.cleaned_data['task']
            task.hours_spent += form.cleaned_data['hours']
            task.save()

            return HttpResponse("OK!!")

        return HttpResponse("rompiste todo")
