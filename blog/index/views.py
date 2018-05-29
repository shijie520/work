from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.创建应用
from . import models

def date(request):  #请求
	acts = models.date.objects.all() #获取数据库，返回一张表单 
	return render(request,'homepage.html',{'acts': acts})#返回一个页面，链接acts 键值获取里面表单


def date_page(request,date_page_id):
	act = models.date.objects.get(pk = date_page_id)
	return render(request,'date_page.html',{'act': act})


def edit_page(request,edit_page_id= 0):
	if str(edit_page_id) =='0':
		return render(request,'edit_page.html')
	else:
		act = models.data.objects.get(pk= edit_page_id)
		return render(request,'edit_page.html',{'act': act})




def page_post(request):
	title = request.POST.get('title', 'name')#获取前端数据
	content = request.POST.get('content','content')

	olds = models.date.objects.all()#获取全部数据	
	if title == 'name' :#不能让用户使用默认值
		return HttpResponse('Input of The Error')
	elif title == '':#判断是否为空
		return HttpResponse('Can"t be empty')
	elif content == '':#判断内容是否为空
		return HttpResponse('Can"t be empty')
	for old in olds:#数据库遍历
		if title == old.title:#判断是否重复提交
			return HttpResponse(' already The title submitted it')
	else:#一切OK准备创建
		data = models.date.objects.create(title=title,content=content)
		acts = models.date.objects.all()#创建成功重新刷新页面获取数据
		return render(request,'homepage.html',{'acts': acts})

