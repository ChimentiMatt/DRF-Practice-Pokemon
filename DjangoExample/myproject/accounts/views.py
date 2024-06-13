# from rest_framework import generics, permissions
# from django.contrib.auth import get_user_model
# from rest_framework_simplejwt.views import TokenObtainPairView
# from django.http import JsonResponse

# from .serializers.account_serializers import TrainerSerializer
# from api.models.pokemon import Pokemon

# User = get_user_model()

# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = TrainerSerializer
#     permission_classes = [permissions.AllowAny]

# class CustomTokenObtainPairView(TokenObtainPairView):
#     print('in urls')
    # permission_classes = (permissions.AllowAny,)


# @api_view(['GET'])
# def trainers_pokemon(request):
#     trainer = request.user
#     pokemon = Pokemon.objects.all().values('id', 'name', 'description')
#     pokemon = pokemon.filter(trainer=trainer)
#     pokemon = list(pokemon)
#     return JsonResponse(pokemon, safe=False)