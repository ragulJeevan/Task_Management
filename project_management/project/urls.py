from django.urls import path
from project_management.project.views import ProjectList, ProjectDetail

urlpatterns = [
     path('project_detail/', ProjectList.as_view(), name='project-list'),
     path('project_detail/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
]