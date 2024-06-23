from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render

from ..models.species import Species
from ..serializers.species_serializers import SpeciesSerializer

@api_view(['GET'])
def species_list(request):
    species = Species.objects.all().order_by('pokedex_id')
    species_serializer = SpeciesSerializer(species, many=True)    
    return JsonResponse(species_serializer.data, safe=False)

@api_view(['GET'])
def species_detail(request, pokemon_name):
    species = get_object_or_404(Species, name=pokemon_name)
    serializer = SpeciesSerializer(species)
    return JsonResponse(serializer.data)
