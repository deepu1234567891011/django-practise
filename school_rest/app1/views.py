from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializer import students_serializer
from .models import students
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def new_student(request):
    serializer_std = students_serializer(data=request.data)
    if serializer_std.is_valid():
        serializer_std.save()
        return Response({'message':'one student created successfully!!'})
    else:
        return Response({'message':'invalid details', 'errors': serializer_std.errors})

@api_view(['GET'])
def get_students(request):
    all_students=students.objects.all()
    serializer = students_serializer(all_students,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_single_student(request,id):
    one_student=students.objects.get(id=id)
    serializer=students_serializer(one_student)
    return Response(serializer.data)

@api_view(['PUT','PATCH'])
@authentication_classes([])
@permission_classes([AllowAny])
def update_student(request,id):
    one_student=students.objects.get(id=id)
    partial=True if request.method == 'PATCH' else False
    serializer=students_serializer(one_student,data=request.data,partial=partial)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
@authentication_classes([])
@permission_classes([AllowAny])
def delete_student(request,id):
    one_studnet=students.objects.get(id=id)
    one_studnet.delete()
    return Response({"message:""Student Deleted"})