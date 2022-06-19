from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import TeamSerializer, PlayerSerializer, StaffSerializer
from api.serializers import StartingSerializer, AgeSerializer
from .models import Team, Player, Staff
from django.db.models import Count, Max, Avg, Min


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
        result = {'The quantity of starting players is':len(starting_count)}
        return Response (result)

# Team w/ more players

@api_view(['GET'])
def team_more_players(request):
    if request.method == 'GET':
        teamName_id = 'teamName_id'
        more_player = Player.objects.values('teamName_id').annotate(Count('id'))
        print(more_player)
        result = {'The teams id with more player is ': (more_player[0]['teamName_id'])}
        return Response(result)

# Avg players/team

@api_view(['GET'])
def avg_team_players(request):
    if request.method == 'GET':
        avg_player = Player.objects.values('teamName_id').annotate(players_avg=Avg('id'))
        result = {'The avg team players are ': (avg_player)}
        return Response(result)

# Avg Starting players/team

@api_view(['GET'])
def avg_start_players(request):
    if request.method == 'GET':
        count_start = Player.objects.values('teamName_id','name').filter(is_starting=False).annotate(count=Count('id')).aggregate(Avg('count'))
        result      = {'The avg team players are ': (count_start)}
        return Response(result)

# Oldest Player

@api_view(['GET'])
def player_age_older(request):
    if request.method == 'GET':
        oldest_player = Player.objects.values('name','birthDate').order_by('birthDate').first()
        result = {'The oldest player is ': (oldest_player)}
        return Response(result)

# Youngest Player

@api_view(['GET'])
def player_age_younger(request):
    if request.method == 'GET':
        youngest_player = Player.objects.values('name','birthDate').order_by('-birthDate').first()
        result = {'The youngest player is ': (youngest_player)}
        return Response(result)

# Oldest DT

@api_view(['GET'])
def dt_age_older(request):
    if request.method == 'GET':
        oldest_dt = Staff.objects.filter(Role = 'DT').values('name','birthDate').order_by('birthDate').first()
        result = {'The oldest DT is ': (oldest_dt)}
        return Response(result)
