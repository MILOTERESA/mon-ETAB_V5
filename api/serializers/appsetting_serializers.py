from rest_framework import serializers

from school.models.app_settings import AppSettingModel



class AppSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppSettingModel
        fields = "__all__"