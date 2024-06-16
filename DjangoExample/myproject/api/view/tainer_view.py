from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import TrainerSerializer
from django.http import JsonResponse

@api_view(['GET'])
def trainer_details(request):
    trainer = request.user
    serializer = TrainerSerializer(trainer)
    print('\n\ninnnnn', serializer.data)
    return JsonResponse(serializer.data)

