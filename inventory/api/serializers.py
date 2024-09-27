from rest_framework import serializers
from inventory.models import Inventory_Items
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        # Hash the password before saving it
        user = User(
            username=validated_data['username'],
            password=make_password(validated_data['password'])  # Password should be hashed
        )
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory_Items
        fields = '__all__' 
