from user.models.role_user import RoleUserModel
from api.serializers.role_serializers import RoleUserSerializer
from rest_framework import viewsets



class RoleUserViewSet(viewsets.ModelViewSet):
    queryset = RoleUserModel.objects.all()
    serializer_class = RoleUserSerializer