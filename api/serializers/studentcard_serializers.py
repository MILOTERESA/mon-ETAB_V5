from rest_framework import serializers
from student.models.card import StudentCardModel


class StudentcardSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentCardModel
        fields = "__all__"