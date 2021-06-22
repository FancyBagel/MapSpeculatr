from .serializers import LocationSerializer, MapSerializer
from .models import Location, Map
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
import random

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

    def location(self, request, id, no):
        if Map.objects.filter(id=id).count() == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        map = Map.objects.get(id=id)
        
        ls = Location.objects.filter(map=map)
        #print(ls.count())
        li = list(ls)
        #print(li[0].lat)
        print(len(li))
        if no >= len(li):
            return Response(status=204)
        loc = li[no]
        print(loc.lat)

        json = {"lat": loc.lat, "lng": loc.lng}

        print(json)

        #json = LocationSerializer(ls, many=True)
        return Response(json)
