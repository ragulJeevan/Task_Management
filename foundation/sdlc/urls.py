from django.urls import path
from foundation.sdlc.views import SdlcList, SdlcDetail

urlpatterns = [
     path('sdlc_detail/', SdlcList.as_view(), name='sdlc-list'),
     path('sdlc_detail/<int:pk>/', SdlcDetail.as_view(), name='sdlc-detail'),
]