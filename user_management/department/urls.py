from django.urls import path
from user_management.department.views import DepartmentList, DepartmentDetail

urlpatterns = [
    path('departments/', DepartmentList.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentDetail.as_view(), name='department-detail'),
]
