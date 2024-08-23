from django.urls import path
from foundation.stage.views import StageList, StageDetail

urlpatterns = [
     path('stage_detail/', StageList.as_view(), name='stage-list'),
     path('stage_detail/<int:pk>/', StageDetail.as_view(), name='stage-detail'),
]