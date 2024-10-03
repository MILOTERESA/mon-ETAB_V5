from student.models.card import StudentCardModel
from api.serializers.studentcard_serializers import StudentcardSerializer
from rest_framework import viewsets



class StudentcardViewSet(viewsets.ModelViewSet):
    queryset = StudentCardModel.objects.all()
    serializer_class = StudentcardSerializer