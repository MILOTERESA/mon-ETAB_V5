from rest_framework import viewsets
from api.serializers.teacher_serializers import TeacherSerializer
from professors.models.teacher import TeacherModel


class TeacherViewSet(viewsets.ModelViewSet):

    queryset= TeacherModel.objects.all()
    serializer_class= TeacherSerializer
    