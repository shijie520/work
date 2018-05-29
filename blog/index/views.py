from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models
def date(request):
	acts = models.date.objects.all()
	return render(request,'homepage.html',{'acts': acts})


def date_page(request,date_page_id):
	act = models.date.objects.get(pk = date_page_id)
	return render(request,'date_page.html',{'act': act})


def edit_page(request):
	return render(request,'edit_page.html')


def page_post(request):
	title = request.POST.get('title', 'name')
	content = request.POST.get('content','content')
	olds = models.date.objects.all()	
	if title == 'name' :
		return HttpResponse('Input of The Error')
	elif title == '' and content == '':
		return HttpResponse('Can"t be empty')
	elif content == '':
		return HttpResponse('Can"t be empty')
	for old in olds:
		if title == old.title:
			return HttpResponse(' already The title submitted it')
	else:
		data = models.date.objects.create(title=title,content=content)
		acts = models.date.objects.all()
		return render(request,'homepage.html',{'acts': acts})

