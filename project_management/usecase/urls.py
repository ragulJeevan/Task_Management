from django.urls import path
from project_management.usecase.views import UsecaseList, UsecaseDetail

urlpatterns = [
     path('usecase_detail/', UsecaseList.as_view(), name='usecaes-list'),
     path('usecase_detail/<int:pk>/', UsecaseDetail.as_view(), name='task-detail'),
]