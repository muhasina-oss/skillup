from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from accounts.serializers import UserSerializer,TrainerProfileSerializer
from accounts.models import User
from accounts.permissions import IsTrainer

# Create your views here.

class TrainerRegisterView(APIView):
  
  def post(self,request):
    
    form_data = request.data
    
    serializer_instance = UserSerializer(data=form_data)
    
    if serializer_instance.is_valid():
      
      cleaned_data = serializer_instance.validated_data
      
      instance = User.objects.create_superuser(role="trainer",**cleaned_data)
      
      serializer_instance = UserSerializer(instance)
      
      return Response(data=serializer_instance.data)
    
    else:
      
      return Response(data=serializer_instance.errors)
    
class StudentRegisterView(APIView):
  
  def post(self,request):
    
    form_data = request.data
    
    serializer_instance = UserSerializer(data=form_data)
    
    if serializer_instance.is_valid():
      
      cleaned_data = serializer_instance.validated_data
      
      instance = User.objects.create_user(**cleaned_data)
      
      serializer_instance = UserSerializer(instance)
      
      return Response(data=serializer_instance.data)
    
    else:
      
      return Response(data=serializer_instance.errors)
    
class TrainerProfileDetailView(APIView):
  
  authentication_classes = [authentication.TokenAuthentication]
  
  permission_classes = [permissions.IsAuthenticated,IsTrainer]
  
  def get(self,request):
    
    instance = request.user.trainer
    
    serializer_instance = TrainerProfileSerializer(instance)
    
    return Response(data=serializer_instance.data)
  
class TrainerProfileUpdateView(APIView):
  
  authentication_classes = [authentication.TokenAuthentication]
  
  permission_classes = [permissions.IsAuthenticated,IsTrainer]
  
  def put(self,request,pk=None):
    
    form_data = request.data
    
    instance = request.user.trainer
    
    serializer_instance = TrainerProfileSerializer(data=form_data,instance=instance)
    
    if serializer_instance.is_valid():
      
      serializer_instance.save()
      
      return Response(data=serializer_instance.data)
    
    else:
      
      return Response(data=serializer_instance.errors)
      
      
  