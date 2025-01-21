from django.shortcuts import render
from django.contrib.auth.models import User 
from rest_framework import generics
from .serializers import UserSerializers
from rest_framework.permissions import IsAuthenticated , AllowAny 
 # Create your views here.

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all() # This will get all the users from the database
    serializer_class = UserSerializers # This will serialize the data
    permission_classes = (AllowAny,) # This will allow any user to create an account