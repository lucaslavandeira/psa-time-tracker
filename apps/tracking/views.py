from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
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
            'form': LoadHours(auto_id=False),
        }

        return render(request, 'project_detail.html', context)



def post(request, project, task):
    project = Project.objects.get(id=project)
    form = LoadHours(request.POST)
    task = project.task_set.get(id=task)
    if form.is_valid():
        task.hours_spent += int(form.cleaned_data['hours'])
        task.save()

        return HttpResponseRedirect(reverse('project-detail', kwargs={'project': project.id}))

    return HttpResponse("rompiste todo")
