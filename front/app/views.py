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

		if 'player_id' not in request.session:
			return redirect('/login')

		r=requests.get('http://10.56.4.216:8000/api/app?format=json')
		m = []
		for e in r.json():
			m.append(e['name'])
		context = {
			"maps" : r.json(),
		}
		return render(request, 'maps.html', context)

	def play(self, request):
		if 'player_id' not in request.session:
			return redirect('/login')

		r=requests.get('http://10.56.1.171:8000/play/' + str(request.session['player_id']))
		if r.status_code != 200:
			return redirect('/maps')
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

		return RResponse(r.json())

	def send(self, request):
		if 'player_id' not in request.session:
			return redirect('/login')
		r=requests.post('http://10.56.1.171:8000/play/' + str(request.session['player_id']), data=json.dumps(request.data), headers={'content-type': 'application/json'})
		return RResponse(data=r.json())

	def new(self, request, map):
		if 'player_id' not in request.session:
			return redirect('/login')
		r=requests.get('http://10.56.1.171:8000/new/' + str(map) + '/' + str(request.session['player_id']))
		return redirect('/play')

	def index(self, request):
		if 'player_id' not in request.session:
			return redirect('/login')
		return render(request, 'index.html')

	def confirm(self, request):
		if 'player_id' not in request.session:
			return redirect('/login')

		data=json.dumps(request.data)
		r=requests.post(url='http://10.56.4.216:8000/api/app', data=data, headers={'content-type': 'application/json'})
		return render(request, 'index.html') #cokolwiek
	
	def login(self, request):
		return render(request, 'login.html')
	
	def verify(self, request):
		dict = {}
		dict['name'] = request.POST['name']
		dict['password'] = request.POST['password']
		data = json.dumps(dict)
		r=requests.get(url='http://10.56.7.90:8000/login', data=data, headers={'content-type': 'application/json'})
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
		if password != rep or len(password) < 3 or len(name) < 3:
			return redirect('/register')
		
		dict = {}
		dict['name'] = name
		dict['password'] = password 
		data = json.dumps(dict)
		r=requests.get(url='http://10.56.7.90:8000/register', data=data, headers={'content-type': 'application/json'})
		if r.status_code != 200:
			return redirect('/register') 
		return redirect('/main')
	
	def logout(self, request):
		if 'player_id' in request.session:
			del request.session['player_id']
		return redirect('/main')

	
	def map_info(self, request, map_id):
		if 'player_id' not in request.session:
			return redirect('/login')

		r=requests.get(url='http://10.56.4.216:8000/api/details/' + str(map_id))
		if r.status_code != 200:
			return redirect('/main')
		data = r.json()

		user_ids = []
		for stat in data:
			user_ids.append(stat['user_id'])

		r=requests.get(url='http://10.56.7.90:8000/user_names', data=json.dumps(user_ids), headers={'content-type': 'application/json'})
		dict = json.loads(r.json())
		for i in range(0, len(data)):
			data[i]['username'] = dict[i]

		context = {
			'stats': data
		}
		return render(request, 'details.html', context)


	def user_info(self, request, user_id):
		if 'player_id' not in request.session:
			return redirect('/login')
		
		r=requests.get(url='http://10.56.7.90:8000/user_info/'+str(user_id))
		if r.status_code != 200:
			return redirect('/main')
		context = {
			'info': r.json()
		}
		return render(request, 'user_info.html', context)
		