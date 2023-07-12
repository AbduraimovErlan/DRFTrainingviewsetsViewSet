from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('ViewSet1.urls')),
    path('api/v1/', include('ViewSet2.urls')),
    path('api/v1/', include('ViewSet3.urls')),
    path('api/v1/', include('ViewSet4.urls')),
    path('api/v1/', include('ViewSet5.urls')),
    path('api/v1/', include('ViewSet6.urls')),
    path('api/v1/', include('ViewSet7.ulrs')),
    path('api/v1/', include('ViewSet8.urls')),
    path('api/v1/', include('ViewSet9.urls')),
    path('api/v1/', include('ViewSet10.urls')),
]
