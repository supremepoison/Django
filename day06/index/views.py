from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
# Create your views here.

def request_views(request):
    print(request.META)

    scheme = request.scheme
    body = request.body
    path = request.path
    host = request.get_host()
    method = request.method
    get = request.GET
    post = request.POST
    cookies = request.COOKIES

    return render(request,'01-request.html',locals())

def referer_views(request):
    #获取请求源地址,如果没有返回/
    referer= request.META.get('HTTP_REFERER','/')
    return HttpResponse(referer)

def login_views(request):
    if request.method == 'GET':
        return render(request,'03-login.html')
    else:
        uname = request.POST['uname']
        upwd = request.POST['upass']
        print(uname,upwd)
        return HttpResponse(1111)

def form_views(request):
    if request.method == 'GET':

        form = RemarkForm()
        return render(request,'04-form.html',locals())
    else:
        #1.通过RemarkForm的构造函数,接受请求提交数据
        form = RemarkForm(request.POST)
        #2.通过验证
        if form.is_valid():
        #3.通过验证后,取值
            cd = form.cleaned_data
            print(cd)
        return HttpResponse('Yeah')


def modelform_views(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request,'05-register.html',locals())
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(**form.cleaned_data)
            print(user.uname,user.upwd,user.uemail)
        return HttpResponse('Ha')