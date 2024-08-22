from django.urls import path, include

urlpatterns = [
    path('status/', include('foundation.status.urls')),
    # path('type/', include('foundation.type.urls')),
    # path('source/', include('foundation.source.urls')),
    # path('stage/', include('foundation.stage.urls')),
    # path('sdlc/', include('foundation.sdlc.urls')),
    # path('complexity/', include('foundation.complexity.urls')),
    # path('priority/', include('foundation.priority.urls')),
]