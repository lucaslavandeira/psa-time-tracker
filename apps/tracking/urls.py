from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello, name="tracker"),
    path('projects/<int:project>', views.ProjectDetail.as_view(), name='project-detail'),
    path('projects/<int:project>/<int:task>', views.post, name='update-project'),
]
