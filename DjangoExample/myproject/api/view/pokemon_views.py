from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.db.models import Count
from ..models.pokemon import Pokemon
from ..serializers.pokemon_serializers import PokemonSerializer
from django.http import JsonResponse
from django.shortcuts import render
from ..models.species import Species
from ..serializers.species_serializers import SpeciesSerializer

class PokemonListView(generics.ListAPIView):

    def list(self):
        pokemon = Pokemon.objects.all().values('id', 'name', 'description')
        items_list = list(pokemon)
        return JsonResponse(items_list, safe=False)

# def pokemon_list(request):
#     pokemon = Pokemon.objects.all().values('id', 'name', 'description')
#     items_list = list(pokemon)
#     return JsonResponse(items_list, safe=False)

def pokemon_detail(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    serializer = PokemonSerializer(pokemon)
    return JsonResponse(serializer.data)

def pokemon_caught_count(request, pokemon_name):
    pokemon = Pokemon.objects.all()
    species = Species.objects.all()
    species = species.filter(name=pokemon_name)
    pokemon = pokemon.filter(name=pokemon_name)
    serializer = PokemonSerializer(pokemon)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def trainers_pokemon(request):
    trainer = request.user
    pokemon = Pokemon.objects.all().values('id', 'name', 'description', 'species__name', 'poke_type__name', 'poke_type', 'species')
    pokemon = pokemon.filter(trainer=trainer)
    pokemon = list(pokemon)
    return JsonResponse(pokemon, safe=False)


class PokemonCountView(generics.ListAPIView):
    serializer_class = PokemonSerializer

    def get_queryset(self):
        return Pokemon.objects.all()
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        count = sum(1 for poke in queryset if str(poke.species) == kwargs.get('pokemon_name'))
        return JsonResponse(count, safe=False)
    