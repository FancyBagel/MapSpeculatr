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

class FrontViewSet(viewsets.ViewSet):
	def list(self, request):

		#if 'player_id' in request.session:
		#	return redirect('/play')
		

		r=requests.get('http://host.docker.internal:8000/api/app?format=json')

		#print(r.json())
		m = []
		for e in r.json():
			m.append(e['name'])
			#print(e['name'])

		#return re(request, 'addmap.html')
		#return HttpResponse(r.json())

		context = {
			"maps" : r.json(),
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

		print(type(request.data))
		#print((json.dumps(data)))

		r=requests.post('http://host.docker.internal:8002/play/' + str(request.session['player_id']), data=json.dumps(request.data), headers={'content-type': 'application/json'})

		print(r.json())
		#print(type(json.loads(r.json())))
		#print(json.loads(r.json())['lat'])

		return RResponse(data=r.json())

	def new(self, request, map):
		if 'player_id' not in request.session:
			return redirect('/login')

		r=requests.get('http://host.docker.internal:8002/new/' + str(map) + '/' + str(request.session['player_id']))

		#print(type(json.loads(r.json())))
		#print(json.loads(r.json())['lat'])

		return redirect('/play')

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
		data = json.loads(r.json())
		request.session['player_id'] = data['id']
		return redirect('/main')

	def register(self, request):
		return render(request, 'register.html')
	
	def verify_register(self, request):
		name = request.POST['name']
		password = request.POST['password']
		rep = request.POST['rep']
		if password != rep:
			return redirect('/register')
		
		dict = {}
		dict['name'] = name
		dict['password'] = password 
		data = json.dumps(dict)
		r=requests.get(url='http://host.docker.internal:8003/register', data=data, headers={'content-type': 'application/json'})
		if r.status_code != 200:
			return redirect('/register') 
		return redirect('/main')
	
	def logout(self, request):
		if 'player_id' in request.session:
			del request.session['player_id']
		return RResponse("OK")