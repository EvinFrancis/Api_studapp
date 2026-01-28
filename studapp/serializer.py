from rest_framework import serializers
from studapp.models import Studentdb

class student_serializer(serializers.ModelSerializer):
    class Meta:
        model=Studentdb
        fields=(
            
            "Name",
            "place",
            "course",
            "mobile"
        )
