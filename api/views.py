
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api import serializers
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Team
import json

# Create your views here.
class HelloApiView(APIView):
    # API test
    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        # Return characteristics list
        an_apiview =[
            'Using HTTP methods like GET, POST, PUT, DELETE',
            'Is like a Djangos view',
            'We can have the control about logical of the APP',
            'is mapping manually to URLs'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
    def post(self,request):
        # Message Name
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
class TeamView(View):
    #Evadir autorizaciones
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    #-------------GET-------------
    def get(self,request,id=0):
        if (id>0):
           teams=list(Team.objects.filter(id=id).values())
           if len(teams)>0:
               team=teams[0]
               datos={'message':"Success",'team':team}
           else:
               datos={'message':"No se encontraron Equipos"}
           return JsonResponse(datos)
        teams = list(Team.objects.values())
        if len(teams)>0:
            datos={'message':"Success",'teams':teams}
        else:
            datos={'message':"No se encontraron Equipos"}
        return JsonResponse(datos)
    #-------------POST-------------
    def post(self,request):
        # print(request.body)
        jd = json.loads(request.body)
        print(jd)
        Team.objects.create(name=jd['name'],flag=jd['flag'],shield=jd['shield'])
        datos={'message':"Success"}
        return JsonResponse(datos)
    #-------------PUT-------------
    def put(self,request,id):
        jd = json.loads(request.body)
        teams=list(Team.objects.filter(id=id).values())
        if len(teams)>0:
           team=Team.objects.get(id=id)
           team.name=jd['name']
           team.flag=jd['flag']
           team.shield=jd['shield']
           team.save()
           datos={'message':"Success"}
        else:
            datos={'message':"No se encontraron Equipos"}
        return JsonResponse(datos)


    # -------------DELETE-------------
    def delete(self,request):
        pass