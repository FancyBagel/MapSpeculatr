from django.shortcuts import render
#import requests

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