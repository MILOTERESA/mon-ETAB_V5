from rest_framework import serializers

from user.models.user import CustomUserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ["username","password"]