from rest_framework import viewsets
from api.serializers.student_serializers import StudentSerializer
from student.models.student import StudentModel


class StudentViewSet(viewsets.ModelViewSet):

    queryset= StudentModel.objects.all()
    serializer_class= StudentSerializer
    