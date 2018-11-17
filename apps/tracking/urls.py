from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name="tracker"),
    path('projects/<int:project>', views.project_detail, name='project-detail'),
    path('projects/<int:project>/<int:task>', views.TaskView.as_view(), name='update-task'),
]
