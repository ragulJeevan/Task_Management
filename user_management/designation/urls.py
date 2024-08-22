from django.urls import path
from user_management.designation.views import DesignationList, DesignationDetail

urlpatterns = [
    path('designations/', DesignationList.as_view(), name='designation-list'),
    path('designations/<int:pk>/', DesignationDetail.as_view(), name='designation-detail'),
]
