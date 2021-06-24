import json
from django.shortcuts import render, redirect
import requests
from requests.api import head
from requests.models import Response
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.response import Response as RResponse

# Create your views here.

def addmap(request):

	
	return render(request, 'addmap.html')

#def sendtomaps(request):
#
#    requests.post("http://127.0.0.1/api/v1/emails/send/", data={
#        "receiver": order.customer_email,
#        "subject": "Order Created",
#        "body": "Hello %s, your order has been created. Total of: %s. Thanks" % (order.customer_name, order.total)
#    })
#
#    return render(request, 'addmap.html')

class FrontViewSet(viewsets.ViewSet):
	def list(self, request):

		#if 'player_id' in request.session:
		#	return redirect('/play')
		

		r=requests.get('http://host.docker.internal:8000/api/app?format=json')

		#print(r.json())
		m = []
		for e in r.json():
			m.append(e['name'])
			print(e['name'])

		#return re(request, 'addmap.html')
		#return HttpResponse(r.json())

		context = {
			"maps" : m,
		}

		return render(request, 'maps.html', context)

	def play(self, request):
		if 'player_id' not in request.session:
			return redirect('/maps')
		#context = {
		#	"x" : 265767676767435.35,
		#}
		#return render(request, 'play.html', context)

		r=requests.get('http://host.docker.internal:8002/play/' + str(request.session['player_id']))
		#print(r.json())

		response = r.json()

		if response['status'] == 'game_on':
			context = {
				'lat' : response['data']['lat'],
				'lng' : response['data']['lng'],
			}
			return render(request, 'play.html', context)
		if response['status'] == 'game_finished':
			context = {
				'distance' : response['result']
			}
			return render(request, 'finished.html', context)

		#print(type(r.json()))

		return RResponse(r.json())

	def send(self, request):
		if 'player_id' not in request.session:
			return redirect('/maps')
		#context = {
		#	"x" : 265767676767435.35,
		#}
		#return render(request, 'play.html', context)

		data={'lat': 2137,'lng': 2137}

		print(type(request.data))
		#print((json.dumps(data)))

		r=requests.post('http://host.docker.internal:8002/play/' + str(request.session['player_id']), data=json.dumps(request.data), headers={'content-type': 'application/json'})

		print(r.json())
		#print(type(json.loads(r.json())))
		#print(json.loads(r.json())['lat'])

		return RResponse(data=r.json())

	def new(self, request, map):
		if 'player_id' not in request.session:
			return redirect('/maps')

		r=requests.get('http://host.docker.internal:8002/new/' + str(map) + '/' + str(request.session['player_id']))

		#print(type(json.loads(r.json())))
		#print(json.loads(r.json())['lat'])

		return RResponse()

	def index(self, request):
		#request.session['player_id'] = int(11)
		#if 'player_id' not in request.session:
		#	return redirect('/maps')
		return render(request, 'index.html')

	def confirm(self, request):
		if 'player_id' not in request.session:
		#	return redirect('/maps')
			print('uh-oh')

		data=json.dumps(request.data)
		r=requests.post(url='http://host.docker.internal:8000/api/app', data=data, headers={'content-type': 'application/json'})
		return render(request, 'index.html') #cokolwiek
	
	def login(self, request):
		return render(request, 'login.html')
	
	def verify(self, request):
		dict = {}
		dict['name'] = request.POST['name']
		dict['password'] = request.POST['password']
		data = json.dumps(dict)
		print(data)
		r=requests.get(url='http://host.docker.internal:8003/login', data=data, headers={'content-type': 'application/json'})
		if r.status_code != 200:
			return redirect('/login') 
		print(r.raw)
		request.session['player_id'] = r.raw
		return redirect('')


	
	def logout(self, request):
		if 'player_id' in request.session:
			del request.session['player_id']
		return Response("OK")