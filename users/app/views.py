from .models import User
import json
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.utils import timezone

class UserViewSet(viewsets.ViewSet):
    # Create your views here.
    def register(self, request):
        info = json.loads(request.body)
        newName = info['name']
        password = info['password']
        if not User.objects.filter(name=newName).count() == 0:
            return Response(status=404)

        newUser = User.objects.create(name=newName, password = password, joinDate = timezone.now())
        return Response("OK")

    def login(self, request):
        print(request.body)
        info = json.loads(request.body)
        newName = info['name']
        password = info['password']
        print(newName)
        print(password)

        if User.objects.filter(name=newName).count() == 0:
            return Response(status=404)
        cand = User.objects.get(name=newName)
        if cand.password != password:
            return Response(status=404)

        return Response(data=cand.id, status=200)

    def user_list(self, request):
        list = {}
        list['list'] = []
        for user in User.objects.all():
            list['list'].append({
                'id': user.id,
                'name': user.name,
            })
        return Response(list)

    def user_info(self, request):
        userName = json.loads(request.body)['player_id']
        info = {}
        if User.objects.filter(name = userName).count() == 0:
            return Response(status=404)
        user = User.objects.get(name = userName)
        json = UserSerializer(user)
        return Response(json)
    