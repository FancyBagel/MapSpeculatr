from rest_framework import serializers

from .models import Map, Location, Stat

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['lat', 'lng']
class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ['user_id', 'highscore']