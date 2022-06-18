from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializers import TeamSerializer
from api.serializers import PlayerSerializer
from api.serializers import StaffSerializer
from api.serializers import StartingSerializer
from api.serializers import AgeSerializer
from .models import Team
from .models import Player
from .models import Staff



# Create your views here.

# Master of Teams...

@api_view(['GET', 'POST'])
def team_api_view(request):
    #-------------GET-------------
    if request.method == 'GET':
        teams= Team.objects.all()
        teams_serializer = TeamSerializer(teams,many = True)
        return Response(teams_serializer.data)

    #-------------POST-------------
    elif request.method == 'POST':
          team_serializer = TeamSerializer(data = request.data)
          if team_serializer.is_valid():
            team_serializer.save()
            return Response(team_serializer.data)
          return Response(team_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def team_detail_view(request,pk = None):

    #-------------GET-------------
    if request.method == 'GET':
        team = Team.objects.filter(id = pk).first()
        team_serializer = TeamSerializer(team)
        return Response(team_serializer.data)

    #-------------PUT-------------

    elif request.method == 'PUT':
          request.data
          team = Team.objects.filter(id = pk).first()
          team_serializer = TeamSerializer(team,data=request.data)
          if team_serializer.is_valid():
              team_serializer.save()
              return Response(team_serializer.data)
          return Response(team_serializer.errors)


    # -------------DELETE-------------
    elif  request.method == 'DELETE':
        team = Team.objects.filter(id = pk).first()
        team.delete()
        return Response('¡Deleted!')

# 1----> Team count <-----

@api_view(['GET'])
def team_api_count(request):
    if request.method == 'GET':
        team_count = Team.objects.count()
        content = {'Total Teams: ': team_count}
        return Response(content)

# 2-----> Players Count <-----

@api_view(['GET'])
def player_api_count(request):
    if request.method == 'GET':
        player_count = Player.objects.count()
        content = {'Total Players: ': player_count}
        return Response(content)
# Players Count - is starting

@api_view(['GET'])
def starting_api_count(request):

    if request.method == 'GET':
        starting_count = Player.objects.filter(is_starting = False)
        teams_serializer = StartingSerializer(starting_count,many = True)
        starting_count = teams_serializer.data
        result = {'There is ':len(starting_count)}
        return Response (result)

# Oldest Player

@api_view(['GET'])
def test_age_older(request):

    if request.method == 'GET':
        oldest_player = Player.objects.values('birthDate').all()
        # player_serializer = AgeSerializer(oldest_player,many = True)
        # print(player_serializer)
        result = (oldest_player)
        return Response(result)

# Master of Players...

@api_view(['GET', 'POST'])
def player_api_view(request):
     #-------------GET-------------
    if request.method == 'GET':
        players= Player.objects.all()
        players_serializer = PlayerSerializer(players,many = True)
        return Response(players_serializer.data)
    #-------------POST-------------
    elif request.method == 'POST':
          player_serializer = PlayerSerializer(data = request.data)
          if player_serializer.is_valid():
            player_serializer.save()
            return Response(player_serializer.data)
          return Response(player_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def player_detail_view(request,pk = None):
    #-------------GET-------------
    if request.method == 'GET':
        player = Player.objects.filter(id = pk).first()
        player_serializer = PlayerSerializer(player)
        return Response(player_serializer.data)

    #-------------PUT-------------

    elif request.method == 'PUT':
          request.data
          player = Player.objects.filter(id = pk).first()
          player_serializer = PlayerSerializer(player,data=request.data)
          if player_serializer.is_valid():
              player_serializer.save()
              return Response(player_serializer.data)
          return Response(player_serializer.errors)


    # -------------DELETE-------------
    elif  request.method == 'DELETE':
        player = Player.objects.filter(id = pk).first()
        player.delete()
        return Response('¡Deleted!')

#Master of Staff...

@api_view(['GET', 'POST'])
def staff_api_view(request):
     #-------------GET-------------
    if request.method == 'GET':
        staffs= Staff.objects.all()
        staffs_serializer = StaffSerializer(staffs,many = True)
        return Response(staffs_serializer.data)
    #-------------POST-------------
    elif request.method == 'POST':
          staff_serializer = StaffSerializer(data = request.data)
          if staff_serializer.is_valid():
            staff_serializer.save()
            return Response(staff_serializer.data)
          return Response(staff_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def staff_detail_view(request,pk = None):
    #-------------GET-------------
    if request.method == 'GET':
        staff = Staff.objects.filter(id = pk).first()
        staff_serializer = StaffSerializer(staff)
        return Response(staff_serializer.data)

    #-------------PUT-------------

    elif request.method == 'PUT':
          request.data
          staff = Staff.objects.filter(id = pk).first()
          staff_serializer = StaffSerializer(staff,data=request.data)
          if staff_serializer.is_valid():
              staff_serializer.save()
              return Response(staff_serializer.data)
          return Response(staff_serializer.errors)


    # -------------DELETE-------------
    elif  request.method == 'DELETE':
        staff = Staff.objects.filter(id = pk).first()
        staff.delete()
        return Response('¡Deleted!')