from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from ..view.item_views import *
from ..view.pokemon_views import *
from ..view.tainer_view import *
from ..view.pokedex_view import *
from ..view.pokemon_views import *
from ..view.species_view import *

urlpatterns = [
    # path('items/', include('urls/items.urls')),
    path('trainer/', include('api.app_urls.trainer_urls')),
    path('pokemon/', include('api.app_urls.pokemon_urls')),
    path('pokedex/', include('api.app_urls.pokedex_urls')),
    path('species/', include('api.app_urls.species_urls')),
]


