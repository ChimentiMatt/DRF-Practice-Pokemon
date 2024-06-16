from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from ..models.pokemon import Pokemon
from ..serializers.pokemon_serializers import PokemonSerializer
from django.http import JsonResponse

def pokemon_list(request):
    pokemon = Pokemon.objects.all().values('id', 'name', 'description')
    items_list = list(pokemon)
    return JsonResponse(items_list, safe=False)

@api_view(['GET'])
def trainers_pokemon(request):
    trainer = request.user
    pokemon = Pokemon.objects.all().values('id', 'name', 'description', 'species__name', 'poke_type__name', 'poke_type', 'species')
    pokemon = pokemon.filter(trainer=trainer)
    # print('\n\n',pokemon)
    pokemon = list(pokemon)
    return JsonResponse(pokemon, safe=False)

