from django.urls import path
from .serializers.account_serializers import trainer_detail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path('me/', api.me, name='me'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('trainer/', trainer_detail, name='user-list'),  
]

    # path('signup/', api.signup, name='signup'),