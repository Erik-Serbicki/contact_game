from django.shortcuts import render
from rest_framework import generics, status
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.http import JsonResponse

# View to list all active rooms
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

# View to list all active user
class UserView(generics.ListAPIView):
    queryset = User.objects.all()
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
    serializer_class = CreateUserSerializer
    
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        host = self.request.session.session_key
        
        serializer = self.serializer_class(data=request.data)
        print(f"Initial Data: {serializer.initial_data}")
        
        if serializer.is_valid():
            user_name = serializer.data.get('user_name')
            room_code = serializer.data.get('room_code') 
    
            user_query = User.objects.filter(user=host)
            if user_query.exists():
                user = user_query[0]
                user.user_name = user_name
                user.user = host
                user.room_code = room_code
                user.save(update_fields=['user', 'user_name', 'room_code'])
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
            else:
                user = User(user=host, user_name=user_name, room_code=room_code)
                user.save()
                return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({'Bad Input': 'Invalid Data'}, status=status.HTTP_400_BAD_REQUEST)

class GetUsersInRoom(APIView):
    serializer_class = UserSerializer
    lookup_url_kwarg = 'code'
    
    def get(self, request, format=None):
        code = request.GET.get(self.lookup_url_kwarg)
        if code != None:
            user = User.objects.filter(room_code=code)
            if user.exists():
                data = UserSerializer(user[0]).data
                data['is_host'] = self.request.session.session_key == user[0].user
                return Response(data, status=status.HTTP_200_OK)
            return Response({'Room Not Found': "Invalid Room Code"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"Bad Request":"No Room Input"}, status=status.HTTP_400_BAD_REQUEST)
