from rest_framework import serializers
from student.models.absence import AbsenceModel


class AbsenceSerializers(serializers.ModelSerializer):

    class Meta:
        model = AbsenceModel
        fields = "__all__"