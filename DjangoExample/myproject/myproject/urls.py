from django.contrib import admin
from django.urls import path, include
# from DjangoExample.myproject.api.app_urls.urls import urlpatterns as auth_urls

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    # path('api/', include('api.urls')),
    path('api/', include('api.app_urls.urls')),
    path('admin/', admin.site.urls),
]
