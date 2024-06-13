from rest_framework import serializers
from ..models.gym import Gym

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'