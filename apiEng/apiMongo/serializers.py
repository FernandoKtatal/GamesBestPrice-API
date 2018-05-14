from rest_framework_mongoengine import serializers
from .models import Game

class GameSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Game
        fields = '__all__'