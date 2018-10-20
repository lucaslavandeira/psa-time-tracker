from django.shortcuts import render


def hello(request):
    # Lo busca en la carpeta templates/
    return render(request, 'tracking/tracker.html')
