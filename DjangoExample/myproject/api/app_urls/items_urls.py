from django.urls import path
from ..view.item_views import *

urlpatterns = [
    path('', item_list, name='item-list-create'),
    path('trainer-items/', trainers_items, name='trainer-items'),
]
