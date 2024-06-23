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

class PokemonDetailView(generics.RetrieveAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def retrieve(self, request, *args, **kwargs):
        pokemon = self.get_object()
        serializer = self.get_serializer(pokemon)
        return JsonResponse(serializer.data)

class PokemonCountView(generics.ListAPIView):
    serializer_class = PokemonSerializer

    def get_queryset(self):
        return Pokemon.objects.all()
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        count = sum(1 for poke in queryset if str(poke.species) == kwargs.get('pokemon_name'))
        return JsonResponse(count, safe=False)
    