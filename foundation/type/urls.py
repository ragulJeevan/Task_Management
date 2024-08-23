from django.urls import path
from foundation.type.views import TypeList, TypeDetail

urlpatterns = [
     path('type_detail/', TypeList.as_view(), name='type-list'),
     path('type_detail/<int:pk>/', TypeDetail.as_view(), name='type-detail'),
]