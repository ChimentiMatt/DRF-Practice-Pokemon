from django.urls import path
from ..view.species_view import *

urlpatterns = [
    path('', species_list, name='species'),
    path('<str:pokemon_name>/', species_detail, name='species_detail'),
]
