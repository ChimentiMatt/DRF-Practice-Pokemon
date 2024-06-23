from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models.pokemon import Pokemon
from ..serializers.pokemon_serializers import PokemonSerializer
from django.http import JsonResponse
from django.shortcuts import render


def pokemon_list(request):
    pokemon = Pokemon.objects.all().values('id', 'name', 'description')
    items_list = list(pokemon)
    return JsonResponse(items_list, safe=False)

def pokemon_detail(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    serializer = PokemonSerializer(pokemon)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def trainers_pokemon(request):
    trainer = request.user
    pokemon = Pokemon.objects.all().values('id', 'name', 'description', 'species__name', 'poke_type__name', 'poke_type', 'species')
    pokemon = pokemon.filter(trainer=trainer)
    pokemon = list(pokemon)
    return JsonResponse(pokemon, safe=False)

