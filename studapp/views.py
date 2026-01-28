from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from studapp.models import Studentdb
from studapp import serializer

# Create your views here.
class Student_api(APIView):
    def get(self,request):
        items=Studentdb.objects.all()
        serializer_data=serializer.student_serializer(items,many=True)
        return Response(serializer_data.data,status.HTTP_200_OK,)
    
    def post(self,request):
        python_obj=serializer.student_serializer(data=request.data)
        if python_obj.is_valid():
            python_obj.save()
            return Response("Data saved succesfully...?",status.HTTP_201_CREATED)
        return Response("invalid data.....!",status.HTTP_400_BAD_REQUEST)
    