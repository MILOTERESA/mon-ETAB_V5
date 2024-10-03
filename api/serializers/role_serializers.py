from rest_framework import serializers

from user.models.role_user import RoleUserModel


class RoleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleUserModel
        fields = "__all__"