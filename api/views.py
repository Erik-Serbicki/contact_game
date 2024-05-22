from django.shortcuts import render
from rest_framework import generics, status
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.http import JsonResponse

# View to list all active rooms
class RoomView(generics.ListAPIView):
    query = Room.object.all()
    serializer_class = RoomSerializer

#