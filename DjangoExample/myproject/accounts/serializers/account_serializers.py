from rest_framework import serializers
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response


User = get_user_model()

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')

@api_view(['GET'])
def trainer_detail(request):
    user = request.user
    serializer = TrainerSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)