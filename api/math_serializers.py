from rest_framework import serializers
from api.models import Team, Player, Staff
from api.serializers import TeamSerializer, PlayerSerializer, StaffSerializer

class MorePlayersSerializer(serializers.ModelSerializer):
    teamName = serializers.StringRelatedField()
    class Meta:
        model = Player
        fields = 'teamName_id'