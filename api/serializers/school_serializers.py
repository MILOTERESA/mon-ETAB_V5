from rest_framework import serializers
from school.models.school import SchoolModel


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolModel
        fields = "__all__"