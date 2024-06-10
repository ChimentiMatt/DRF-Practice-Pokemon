from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .view.item_views import *
from .serializers.trainer_serializers import trainer_detail
from . import auth_views


urlpatterns = [
    path('auth/', include(auth_views)),
    path('auth/trainer/', trainer_detail, name='user-list'),   
    path('items/', item_list, name='item-list-create'),
    path('trainer-items/', trainers_items, name='trainer-items'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
]
