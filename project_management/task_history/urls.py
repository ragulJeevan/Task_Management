from django.urls import path
from project_management.task_history.views import TaskHistoryList, TaskHistoryDetail

urlpatterns = [
     path('task_history_detail/', TaskHistoryList.as_view(), name='task-history-list'),
     path('task_history_detail/<int:pk>/', TaskHistoryDetail.as_view(), name='task-history-detail'),
]