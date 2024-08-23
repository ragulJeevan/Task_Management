from django.urls import path
from foundation.complexity.views import ComplexityList, ComplexityDetail

urlpatterns = [
     path('complexity_detail/', ComplexityList.as_view(), name='complexity-list'),
     path('complexity_detail/<int:pk>/', ComplexityDetail.as_view(), name='complexity-detail'),
]