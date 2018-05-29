from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.创建应用
from . import models


def return_home(request):
	#acts = models.date.objects.all() #获取数据库，返回一张表单 
	return render(request,'homepage.html')#返回一个页面，链接acts 键值获取里面表单



def date(request):  #请求
	acts = models.date.objects.all() #获取数据库，返回一张表单 
	return render(request,'homepage.html',{'acts': acts})#返回一个页面，链接acts 键值获取里面表单


def date_page(request,date_page_id):
	act = models.date.objects.get(pk = date_page_id)
	return render(request,'date_page.html',{'act': act})


def edit_page(request,edit_page_id):
	if str(edit_page_id) =='0':
		return render(request,'edit_page.html')
	else:
		acts = models.date.objects.get(pk = edit_page_id)
		return render(request,'edit_page.html',{'acts':acts})




def page_post(request):
	title = request.POST.get('title', 'name')#获取前端数据
	content = request.POST.get('content','content')
	id = request.POST.get('id','0')
	olds = models.date.objects.all()#获取全部数据	
	if title == 'name' :#不能让用户使用默认值
		return HttpResponse('Input of The Error')
	elif title == '':#判断是否为空
		return HttpResponse('Can"t be empty')
	elif content == '':#判断内容是否为空
		return HttpResponse('Can"t be empty')
	else:	
		for old in olds:#数据库遍历
			if content == old.content:#判断是否重复提交
				return HttpResponse(' already The content submitted it')
	
	if id == '0':
		data = models.date.objects.create(title=title,content=content)
		acts = models.date.objects.all()#创建成功重新刷新页面获取数据
		return render(request,'homepage.html',{'acts': acts})

	else:
		acts = models.date.objects.get(pk = id)
		acts.title = title
		acts.content = content
		acts.save()
		return render(request,'date_page.html',{'act': acts})
