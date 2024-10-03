from base.models.adress import AddressModel
from api.serializers.address_serializers import AddressSerializer
from rest_framework import viewsets



class AddressViewSet(viewsets.ModelViewSet):
    queryset = AddressModel.objects.all()
    serializer_class = AddressSerializer
