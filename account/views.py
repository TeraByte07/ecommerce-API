from django.shortcuts import render
from rest_framework import generics
from .models import User, profile, address
from .serializers import (userSerializers, profileSerializers, addressSerializers)

# Create your views here.
class userList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializers
class profileList(generics.ListCreateAPIView):
    queryset = profile.objects.all()
    serializer_class = profileSerializers
class addressList(generics.ListCreateAPIView):
    queryset = address.objects.all()
    serializer_class =addressSerializers

class userDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializers
class profileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = profile.objects.all()
    serializer_class = profileSerializers
class addressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = address.objects.all()
    serializer_class = addressSerializers