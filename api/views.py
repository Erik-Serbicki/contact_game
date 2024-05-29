from django.shortcuts import render
from rest_framework import generics, status
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.http import JsonResponse

# View to list all active rooms
class RoomView(generics.ListAPIView):
    query = Room.objects.all()
    serializer_class = RoomSerializer

# View to list all active user
class UserView(generics.ListAPIView):
    query = User.objects.all()
    serializer_class = UserSerializer
    
# View to create a room
class CreateRoomView(APIView):
    serializer_class = RoomSerializer
    
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        host = self.request.session.session_key
        
        query = Room.objects.filter(host=host)
        if query.exists():
            room = query[0]
            self.request.session['room_code'] = room.code
            room.save()
            return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
        else:
            room = Room(host=host)
            self.request.session['room_code'] = room.code
            room.save()
            return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)


class CreateUserView(APIView):
    serializer_class = UserSerializer  
    
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        host = self.request.session.session_key  
        
        query = User.objects.filter(host=host)
        if query.exists():
            User = query[0]
                     