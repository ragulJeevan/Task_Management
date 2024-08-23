from django.urls import path
from project_management.feature.views import FeatureList, FeatureDetail

urlpatterns = [
     path('feature_detail/', FeatureList.as_view(), name='feature-list'),
     path('feature_detail/<int:pk>/', FeatureDetail.as_view(), name='feature-detail'),
]