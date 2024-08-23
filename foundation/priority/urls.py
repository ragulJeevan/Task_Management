from django.urls import path
from foundation.priority.views import PriorityList, ProrityDetail

urlpatterns = [
     path('priority_detail/', PriorityList.as_view(), name='priority-list'),
     path('priority_detail/<int:pk>/', ProrityDetail.as_view(), name='priority-detail'),
]