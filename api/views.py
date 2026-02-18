from django.shortcuts import render
from django.http import JsonResponse
from teachers.models import Teacher
from .serializers import TeacherSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def teachers_api_view(request):
    if request.method == "GET":
        teachers = Teacher.objects.all()
        serialized_data = TeacherSerializer(teachers, many=True)
        return Response(serialized_data.data, 
                        status=status.HTTP_200_OK)
    elif request.method == "POST":
        query_set = TeacherSerializer(data=request.data)
        if query_set.is_valid():
            query_set.save() # Save the data into DB
            return Response(query_set.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(query_set.errors, 
                            status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE '])
def teacher_detail(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == "GET":
        serialized_data = TeacherSerializer(teacher)
        return Response(serialized_data.data,
                        status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data = request.data
        serial = TeacherSerializer(teacher, 
                                   data=data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_200_OK)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        