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

        info = json.loads(request.body)
        newName = info['name']
        password = info['password']

        if User.objects.filter(name=newName).count() == 0:
            return Response(status=404)
        cand = User.objects.get(name=newName)
        if cand.password != password:
            return Response(status=404)
        dict={}
        dict['id']=cand.id
        data = json.dumps(dict)

        return Response(data, status=200)

    def user_list(self, request):
        list = {}
        list['list'] = []
        for user in User.objects.all():
            list['list'].append({
                'id': user.id,
                'name': user.name,
            })
        return Response(list)

    def user_info(self, request, user_id):
        if User.objects.filter(id = user_id).count() == 0:
            return Response(status=404)
        user = User.objects.get(id = user_id)
        serialized = UserSerializer(user)
        return Response(serialized.data)

    def user_names(self, request):
        id_list = json.loads(request.body)

        name_list = []
        try:
            for id in id_list:
                name_list.append(User.objects.get(id=id).name)

            return Response(json.dumps(name_list))
        except ...:
            return Response(status=404)

    