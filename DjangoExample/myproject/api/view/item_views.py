from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from ..models.item import Item
from ..serializers.item_serializers import ItemSerializer
from django.http import JsonResponse

def item_list(request):
    items = Item.objects.all().values('id', 'name', 'description')
    items_list = list(items)
    return JsonResponse(items_list, safe=False)

@api_view(['GET'])
def trainers_items(request):
    trainer = request.user
    items = Item.objects.all().values('id', 'name', 'description')
    items = items.filter(trainer=trainer)
    items = list(items)
    return JsonResponse(items, safe=False)
