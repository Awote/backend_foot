from django.db.models.base import Model
from rest_framework import fields,serializers
from .models import User


class User_serializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields= ('username','password','first_name','email')