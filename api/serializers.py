from django.db.models import fields
from rest_framework import serializers
from . models import *

class TeamSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeamModel
        fields = '__all__'

class Betserializers(serializers.ModelSerializer):
    class Meta:
        model = BetModel
        fields = '__all__'

class UpcomingMatchesSerializers(serializers.ModelSerializer):
    class Meta:
        model = UpcomingMatche
        fields = '__all__'