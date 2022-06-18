from dataclasses import field
from rest_framework import serializers
from api.models import Team, Player, Staff
from datetime import datetime
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
          model = Team
          fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = '__all__'

class StartingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ['is_starting']
class AgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ['birthDate']