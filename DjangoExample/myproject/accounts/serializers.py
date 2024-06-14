from rest_framework import serializers

from .models import Trainer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ('id', 'name', 'email',)