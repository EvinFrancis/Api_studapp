from rest_framework import serializers
from studapp.models import Studentdb

class student_serializer(serializers.ModelSerializer):
    class Meta:
        models=Studentdb
        field=(
            "studId",
            "Name",
            "place",
            "course",
            "mobile"
        )
