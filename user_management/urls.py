from django.urls import path, include

urlpatterns = [
    path('department/', include('user_management.department.urls')),
    path('designation/', include('user_management.designation.urls')),
    path('user/', include('user_management.user.urls')),
]