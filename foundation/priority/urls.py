from django.urls import path
from foundation.priority.views import PriorityList, PriorityDetail

urlpatterns = [
     path('priority_detail/', PriorityList.as_view(), name='priority-list'),
     path('priority_detail/<int:pk>/', PriorityDetail.as_view(), name='priority-detail'),
]