from django.urls import path
from foundation.status.views import status_list, status_detail

urlpatterns = [
     path('status_detail/', status_list.as_view(), name='status-list'),
     path('status_detail/<int:pk>/', status_detail.as_view(), name='status-detail'),
]