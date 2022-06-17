from dataclasses import field
from rest_framework import serializers
from api.models import Team
from api.models import Player
from api.models import Staff
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