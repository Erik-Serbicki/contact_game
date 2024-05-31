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
        room_code = self.request.session['room_code']  
        
        room_query = Room.objects.filter(code=room_code)
        
        serializer = self.serializer_class(data=request.data)
        print(serializer.initial_data)
        
        if serializer.is_valid():
            user_name = serializer.data.get('user_name')
    
            user_query = User.objects.filter(user=host)
            if user_query.exists():
                user = user_query[0]
                if user_name != None:
                    user.user_name = user_name
                    user.user = host
                    user.save(update_fields=['user_name', 'user'])
                else:
                    user.user = host
                    user.save(update_fields=['user']) 
                self.request.session['user_name'] = user.user_name
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
            else:
                user = User(user=host, user_name=user_name)
                user.save()
                return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Input': 'Invalid Data'}, status=status.HTTP_400_BAD_REQUEST)
                
        