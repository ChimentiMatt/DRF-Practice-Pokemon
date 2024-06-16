from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .view.item_views import *
from .view.pokemon_views import *
from .view.tainer_view import *

urlpatterns = [
    path('items/', item_list, name='item-list-create'),
    path('trainer-items/', trainers_items, name='trainer-items'),
    path('pokemon/', pokemon_list, name='trainer-items'),
    path('trainers-pokemon/', trainers_pokemon, name='trainer-pokemon'),
    path('trainer-details/', trainer_details, name='trainer-details'),
]
