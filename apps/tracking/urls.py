from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello, name="tracker"),
    path('projects/<int:project>', views.ProjectDetail.as_view(), name='project-detail'),
]
