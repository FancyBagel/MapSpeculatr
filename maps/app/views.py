from .serializers import LocationSerializer, MapSerializer
from .models import Location, Map
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class MapViewSet(viewsets.ViewSet):
    def list(self, request):
        
        #map = Map(name="testowa")
        #map.save()

        maps = Map.objects.all()
        json = MapSerializer(maps, many=True)
        return Response(json.data)
    def create(self, request): #TODO DODAWANIE MAPY

        map = Map(name=request.data["name"])
        map.save()

        list = request.data["list"]

        for element in list:
            location = Location(lat=element["lat"], lng=element["lng"], map=map)
            location.save()

        #maps = Map.objects.all()
        #json = MapSerializer(maps, many=True)
        return Response(Location.objects.all().count())
        return Response(json.data)

    def locations(self, request, id):
        map = Map.objects.get(id=id)
        #ls = Location.objects.get(map=map)
        ls = Location.objects.filter(map=map)
        json = LocationSerializer(ls, many=True)
        return Response(json.data)
