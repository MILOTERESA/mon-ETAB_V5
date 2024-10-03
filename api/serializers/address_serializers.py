from rest_framework import serializers
from base.models.adress import AddressModel



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = "__all__"