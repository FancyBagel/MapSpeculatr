from django.shortcuts import render
import requests
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