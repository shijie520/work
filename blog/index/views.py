from django.shortcuts import render
# Create your views here.
from . import models
def date(request):
	acts = models.date.objects.all()
	return render(request,'homepage.html',{'acts': acts})


def date_page(request,date_page_id):
	act = models.date.objects.get(pk = date_page_id)
	return render(request,'date_page.html',{'act':act})


