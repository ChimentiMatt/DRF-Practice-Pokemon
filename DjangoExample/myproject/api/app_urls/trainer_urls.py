from django.urls import path
from ..view.tainer_view import *

urlpatterns = [
    # path('pokemon/', PokemonView.as_view(), name='trainer-pokemon'),
    path('trainers-pokemon/', TrainersPokemonView.as_view(), name='trainer-pokemon'),
    path('details/', TrainerView.as_view(), name='trainer-details'),
]
