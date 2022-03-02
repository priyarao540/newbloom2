from dataclasses import field

from django.forms import ValidationError
from .models import Books, models
from rest_framework import serializers
from django.contrib.auth.models import User
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'last_name',
            'first_name'
            )
        
    def validate(self, attrs):
        username = attrs['username']
        email = attrs['email']

        user = None

        try:
            user = User.objects.get(username=username)

        except:
            pass

        if user:
            raise ValidationError(
                "username already exists"
            )
        
        if username.isalnum():
            raise ValidationError(
                "Username is not alphanumeric "
            )
        
        return attrs


    def create(self, v_data):
        return User.objects.create_user(**v_data)
