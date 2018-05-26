from django.shortcuts import render
#from django.http import HttpResponse
from . import models
# Create your views here.
'''def hello(request):
	return render(request,'first.html',{'hello': 'html and wrold'})'''

def hello(request):
	active = models.active.objects.get(pk=1)
	return render(request,'webapp/first.html',{'active': active})
