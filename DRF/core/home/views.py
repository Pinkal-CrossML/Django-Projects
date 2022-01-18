from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


# Get All data :  http://127.0.0.1:8000/
@api_view(['GET'])
def show(request):
	student_objs = Student.objects.all().order_by('-id')
	serializer = StudentSerializer(student_objs, many=True)
	return Response(serializer.data)


# create new data: http://127.0.0.1:8000/create/
@api_view(['POST'])
def post_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

# Get data by id: http://127.0.0.1:8000/detail/2/
@api_view(['GET'])
def Detail(request, pk):
	student_objs = Student.objects.get(id=pk)
	serializer = StudentSerializer(student_objs, many=False)
	return Response(serializer.data)

# update data by id: http://127.0.0.1:8000/update/2/
@api_view(['POST'])
def Update(request,pk):
    student_objs = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=student_objs,data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

# Delete data by id: http://127.0.0.1:8000/delete/2/
@api_view(['DELETE'])
def Delete(request, pk):
	tasks = Student.objects.get(id=pk)
	tasks.delete()

	return Response('Item succsesfully delete!')
