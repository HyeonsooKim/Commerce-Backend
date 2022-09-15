from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=128, style={'input_type': 'password'})
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password', 'age', 'gender', 'city', 'nationality']