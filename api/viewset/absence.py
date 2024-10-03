from student.models.absence import AbsenceModel
from api.serializers.absence_serializers import AbsenceSerializers
from rest_framework import viewsets



class AbsenceViewSet(viewsets.ModelViewSet):

    queryset = AbsenceModel.objects.all()
    serializer_class = AbsenceSerializers
