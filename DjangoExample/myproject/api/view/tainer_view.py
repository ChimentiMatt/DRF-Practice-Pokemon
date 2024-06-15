from rest_framework.decorators import api_view

from accounts.serializers import TrainerSerializer
from django.http import JsonResponse

@api_view(['GET'])
def trainer_details(request):
    trainer = request.user
    serializer = TrainerSerializer(trainer)
    return JsonResponse(serializer.data)

