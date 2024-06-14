from django.contrib import admin
from django.urls import path, include
from api.urls import urlpatterns as auth_urls

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    # path('', include(auth_urls)),
]
