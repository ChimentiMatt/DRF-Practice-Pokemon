from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from ..models.pokemon import Pokemon
from ..serializers.pokemon_serializers import PokemonSerializer
from django.http import JsonResponse

def pokedex_list(request):
    pokemon = Pokemon.objects.all().values('id', 'name', 'description', 'pokedex_id')
    items_list = list(pokemon)
    items_list = sorted(items_list, key=lambda x: (x['pokedex_id'] is None, x['pokedex_id']))
    return JsonResponse(items_list, safe=False)
