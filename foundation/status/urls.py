from django.urls import path
from foundation.status.views import status_list, status_detail

urlpatterns = [
     path('statuses/', status_list.as_view(), name='department-list'),
     path('statuses/<int:pk>/', status_detail.as_view(), name='department-detail'),
]