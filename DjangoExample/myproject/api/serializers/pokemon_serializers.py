from rest_framework import serializers
from ..models.pokemon import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'

# @api_view(['GET'])
# def trainer_detail(request):
#     user = request.user
#     serializer = TrainerSerializer(user)
#     return Response(serializer.data, status=status.HTTP_200_OK)