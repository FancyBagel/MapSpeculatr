from rest_framework import serializers

from .models import Map, Location

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['lat', 'lng']