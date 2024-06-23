from django.urls import path
from ..view.pokedex_view import *

urlpatterns = [
    path('', pokedex_list, name='pokedex'),
]
