from .serializers import LocationSerializer, MapSerializer, StatSerializer
from .models import Location, Map, Stat
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
import random

class MapViewSet(viewsets.ViewSet):
    def list(self, request):

        maps = Map.objects.all()
        json = MapSerializer(maps, many=True)
        return Response(json.data)
    def create(self, request):
        if len(request.data["name"]) == 0:
            return Response(status=400)

        map = Map(name=request.data["name"])
        map.save()

        list = request.data["list"]
        if len(list) == 0:
            return Response(status=400)

        for element in list:
            location = Location(lat=element["lat"], lng=element["lng"], map=map)
            location.save()

        return Response(Location.objects.all().count())

    def locations(self, request, id):
        map = Map.objects.get(id=id)
        ls = Location.objects.filter(map=map)
        json = LocationSerializer(ls, many=True)
        return Response(json.data)

    def location(self, request, id, no):
        if Map.objects.filter(id=id).count() == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)

        map = Map.objects.get(id=id)
        
        ls = Location.objects.filter(map=map)
        li = list(ls)

        if no >= len(li):
            return Response(status=204)
        loc = li[no]

        json = {"lat": loc.lat, "lng": loc.lng}

        return Response(json)
    
    def details(self, request, id):
        try:
            map = Map.objects.get(id=id)
            to_send = Stat.objects.filter(map = map)
            json = StatSerializer(to_send, many=True)
            return Response(json.data)
        except ...:
            return Response(status=404)
        