from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        # Define the model to use
        model = Room
        
        # Define the fields within the model
        fields = ('id', 'code', 'host', 'created_at')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user', 'user_name', 'room')

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name')