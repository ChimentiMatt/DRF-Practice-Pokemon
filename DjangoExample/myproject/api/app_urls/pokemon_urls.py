from django.urls import path
from ..view.pokemon_views import *

urlpatterns = [
    path('', PokemonListView.as_view(), name='trainer-items'),
    path('<str:pokemon_name>/', PokemonCountView.as_view(), name='trainer-pokemon'),
    path('<int:id>/', PokemonDetailView.as_view(), name='pokemon_detail'),
    path('pokemon-count/<str:pokemon_name>/', PokemonCountView.as_view(), name='trainer-pokemon'),
]