from school.models.school import SchoolModel
from api.serializers.school_serializers import SchoolSerializer
from rest_framework import viewsets



class SchoolViewSet(viewsets.ModelViewSet):

    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer