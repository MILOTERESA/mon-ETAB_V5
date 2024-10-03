from school.models.app_settings import AppSettingModel
from api.serializers.appsetting_serializers import AppSettingSerializer
from rest_framework import viewsets



class App_settingViewSet(viewsets.ModelViewSet):
    queryset = AppSettingModel.objects.all()
    serializer_class = AppSettingSerializer