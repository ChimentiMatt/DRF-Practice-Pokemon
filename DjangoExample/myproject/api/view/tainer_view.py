from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from accounts.serializers import TrainerSerializer
from django.http import JsonResponse
from ..models.pokemon import Pokemon

class TrainerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        trainer = request.user
        serializer = TrainerSerializer(trainer)
        print('\n\n::::::innnnn', serializer.data)
        return JsonResponse(serializer.data)


class TrainersPokemonView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        trainer = request.user
        pokemon = Pokemon.objects.filter(trainer=trainer).values(
            'id', 'name', 'description', 'species__name', 'poke_type__name', 'poke_type', 'species'
        )
        pokemon = list(pokemon)
        return JsonResponse(pokemon, safe=False)