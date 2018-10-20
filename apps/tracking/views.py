from django.http import HttpResponse
from django.shortcuts import render
from .models import Project


def hello(request):
    context = {
        'projects': Project.objects.all()
    }

    return render(request, 'tracker.html', context)


def project_detail(request, project):
    context = {
        'project': Project.objects.get(id=project)
    }

    return render(request, 'project_detail.html', context)
