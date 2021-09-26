from django.shortcuts import render
from rest_framework import request, serializers
from .serializer import User_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from rest_framework.renderers import JSONRenderer
from .models import User
# Create your views here.
@api_view(['POST'])
def create_user(request):
    json_data = json.loads(request.body)
    # print(json_data)
    user_serializer = User_serializer(data=json_data)
    
    if user_serializer.is_valid():
        user_serializer.save()
        return Response(status=200)
    else:
        print(user_serializer.errors)
        return Response(status=200,data = "Пользователь с таким логином уже существует!")
@api_view(["GET"])
def user_info(request):
    username_ = json.loads(request.body)
    print(type(username_.get("username")))
    user= username_.get("username")
    # user = User.objects.filter(username = user)
    # print(User_serializer.data)
    # json_ = JSONRenderer().render(User_serializer.data)
    # print(json_)
    from django.core import serializers
    data = serializers.serialize('json', User.objects.filter(username=user), fields=('username','email','age','shoe_size',"first_name"))

    return Response(status=200,data=json.loads(data)[0].get("fields"))

    
