from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
import json
import requests
from .models import Game
import math
import celery

# Create your views here.
def calc_dist(lat1, lon1, lat2, lon2):
    delta_lat = (lat2 - lat1) * math.pi / 180.0
    delta_lon = (lon2 - lon1) * math.pi / 180.0
    lat1 = lat1 * math.pi / 180.0
    lat2 = lat2 * math.pi / 180.0

    a = (math.sin(delta_lat / 2.0) ** 2) + math.cos(lat1) * math.cos(lat2) * (math.sin(delta_lon / 2.0) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    dis = c * 6371000
    return int(dis)


class ServerViewSet(viewsets.ViewSet):
    def location(self, request, map, player):

        r=requests.get('http://10.56.4.216:8000/api/location/'+str(map))

        return Response(data=r.json(), headers={'content-type': 'application/json'})

    def new(self, request, map, player):

        Game.objects.filter(player=player).delete()

        g=Game(player=player, map=map, lat=0, lng=0, points=0, current=0)
        g.save()

        return Response("ok")

    def play(self, request, player):
        if Game.objects.filter(player=player).count() == 0:
            return Response(status=404)
        g = Game.objects.get(player=player)
        r=requests.get('http://10.56.4.216:8000/api/location/' + str(g.map) + '/' + str(g.current))
        response = {}
        if r.status_code == 404:
            response['status'] = 'no_map'
        if r.status_code == 204:
            response['status'] = 'game_finished'
            response['result'] = g.points
            celery.current_app.send_task('app.tasks.add', [{'id': player, 'result': g.points, 'map': g.map}], queue='maps')
            celery.current_app.send_task('app.tasks.modify', [{'user': player, 'score': g.points}], queue='users')
            g.delete()
        if r.status_code == 200:
            response['status'] = 'game_on'
            response['data'] = {'lat': r.json()['lat'], 'lng': r.json()['lng']}
            g.lat = r.json()['lat']
            g.lng = r.json()['lng']
            g.save()

        return Response(response)

    def answer(self, request, player):
        if Game.objects.filter(player=player).count() == 0:
            return Response(status=404)
        g = Game.objects.get(player=player)
        decoded = json.loads(request.body)

        ans_lat = decoded['lat']
        ans_lng = decoded['lng']

        res = calc_dist(ans_lat, ans_lng, g.lat, g.lng)
        g.points = g.points + res
        g.current = g.current + 1
        g.save()

        resp = {'lat' : ans_lat, 'lng' : ans_lng, 'elat' : g.lat, 'elng' : g.lng}

        return Response(data=resp)
