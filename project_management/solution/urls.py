from django.urls import path
from project_management.solution.views import SolutionList, SolutionDetail

urlpatterns = [
     path('solution_detail/', SolutionList.as_view(), name='solution-list'),
     path('solution_detail/<int:pk>/', SolutionDetail.as_view(), name='solution-detail'),
]