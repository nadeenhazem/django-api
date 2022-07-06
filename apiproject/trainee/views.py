from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework import authtoken,authentication,permissions
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_200_OK,HTTP_406_NOT_ACCEPTABLE
from .models import Trainee
from .serializers import *


# Create your views here.
@api_view(['POST'])
def insert(req):
    if 'name' in req.data and 'address' in req.data and 'sex' in req.data and 'national_num' in req.data:
        print("asdasda")
        trainee = Trainee.objects.create(name=req.data['name'],address=req.data['address'],sex=req.data['sex'],national_num=req.data['national_num'])
        data = Trainers(trainee)
        return Response(data.data,status=HTTP_201_CREATED)
    else:
        return Response({'error':'invalid data'},status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def List(request):
    courses = Trainee.objects.all()
    data = Trainers(courses,many=True)
    return Response(data.data,status=HTTP_200_OK)



@api_view(['GET'])
def GETTRAINEE(request,id):
    course = Trainee.objects.get(id=id)
    data = Trainers(course)
    return Response(data.data)


@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update(req):
    c=Trainers(req.data)
    if('id' in req.data):
        course = Trainee.objects.get(id=req.data['id'])
        if 'name' in req.data or 'address' in req.data or 'sex' in req.data or 'national_num' in req.data:
            if 'name' in req.data:
                course.name = req.data['name']
                print(req.data['address'])
            if 'address' in req.data:
                course.address = req.data['address']
            if 'sex' in req.data:
                course.sex = req.data['sex']
            if 'national_num' in req.data:
                course.national_num = req.data['national_num']
            else:
                return Response({'error': 'no data for update'}, status=HTTP_406_NOT_ACCEPTABLE)
            course.save()
            data = Trainers(course)

        return Response(data.data, status=HTTP_201_CREATED)
    else:
        return Response({'error': 'invalid data'}, status=HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
@authentication_classes ([authentication.TokenAuthentication])
def delete(req,id):
    c=Trainee.objects.filter(id=id).delete()
    return Response({'message':'deleted'}, status=HTTP_200_OK)
