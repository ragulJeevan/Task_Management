from django.urls import path
from project_management.task.views import TaskList, TaskDetail

urlpatterns = [
     path('task_detail/', TaskList.as_view(), name='task-list'),
     path('task_detail/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]