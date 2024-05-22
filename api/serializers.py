from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        # Define the model to use
        model = Room
        
        # Define the fields within the model
        fields = ('id', 'code', 'host', 'name', 'created_at')

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('name')