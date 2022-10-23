from tkinter.ttk import Style
from django.contrib.auth import get_user_model
from django.forms import ValidationError 
from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, min_length=8, required=True, write_only=True, style={"input_type": "password"})
    password2 = serializers.CharField(max_length=20, min_length=8, required=True, write_only=True, style={"input_type": "password"})
    class Meta:
        model = get_user_model()
        fields = ["email", "first_name", "last_name", "password", "password2"]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate_first_name(self, value):
        if(not value):
            raise serializers.ValidationError("first name is required")

        return value 


    def validate_last_name(self, value):
        if(not value):
            raise serializers.ValidationError("last name is required")
        
        return value

    def validate(self, data):
        if(data["password"] != data["password2"]):
            raise serializers.ValidationError("Password didn't match")
        
        return data

    def create(self, validated_data):
        user = get_user_model().objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user