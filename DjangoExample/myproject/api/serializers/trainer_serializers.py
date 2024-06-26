# views.py
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer

class TrainerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

