import json
from django.shortcuts import render, redirect
import requests
from requests.api import head
from requests.models import Response
from rest_framework import viewsets
from django.http import HttpResponse

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
		#if 'player_id' not in request.session:
		#	return redirect('/maps')
		context = {
			"x" : 265767676767435.35,
		}
		return render(request, 'play.html', context)
	def index(self, request):
		request.session['player_id'] = int(11)
		if 'player_id' not in request.session:
			return redirect('/maps')
		return render(request, 'index.html')

	def confirm(self, request):
		if 'player_id' not in request.session:
		#	return redirect('/maps')
			print('uh-oh')

		data=json.dumps(request.data)
		r=requests.post(url='http://host.docker.internal:8000/api/app', data=data, headers={'content-type': 'application/json'})
		return render(request, 'index.html') #cokolwiek