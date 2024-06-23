from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .view.item_views import *
from .view.pokemon_views import *
from .view.tainer_view import *
from .view.pokedex_view import *
from .view.pokemon_views import *
from .view.species_view import *

urlpatterns = [
    path('items/', item_list, name='item-list-create'),
    path('trainer-items/', trainers_items, name='trainer-items'),
    path('pokemon/', PokemonListView.as_view(), name='trainer-items'),
    path('pokemon-count/<str:pokemon_name>/', PokemonCountView.as_view(), name='trainer-pokemon'),

    path('trainers-pokemon/', trainers_pokemon, name='trainer-pokemon'),
    path('trainer-details/', trainer_details, name='trainer-details'),
    path('pokedex/', pokedex_list, name='pokedex'),
    path('pokemon/<str:pokemon_name>/', pokemon_detail, name='pokemon_detail'),
    path('species/', species_list, name='species'),
    path('species/<str:pokemon_name>/', species_detail, name='species_detail'),
]
