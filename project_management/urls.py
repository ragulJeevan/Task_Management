from django.urls import path, include

urlpatterns = [
    path('project/', include('project_management.project.urls')),
    path('solution/', include('project_management.solution.urls')),
    path('feature/', include('project_management.feature.urls')),
    path('usecase/', include('project_management.usecase.urls')),
    path('task/', include('project_management.task.urls')),
    path('task_history/', include('project_management.task_history.urls')),
]