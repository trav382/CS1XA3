from django.shortcuts import render

from django.http import HttpResponse


def hello_world(request):

	html = "<html> <body> Hello Worl  d</body> </html>"
	return HttpResponse(html)





# Create your views here.
