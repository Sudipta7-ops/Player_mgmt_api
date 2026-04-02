from rest_framework import serializers
from .models import Player
class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model=Player
        fields='__all__'

    def validate_age(self,value):
        if value<=0:
            raise serializers.ValidationError("Age must be positive")
        return value