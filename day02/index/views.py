from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.


def login_views(request):
    return  HttpResponse('login')

def register_views(request):
    return  HttpResponse('register')

def index_views(request):
    return  HttpResponse('index')

def temp_views(request):
    #1.通过loader
    t = loader.get_template('01-temp.html')
    #2.将模板渲染成字符串
    html = t.render()
    #3.将字符串通过HttpResponse响应给客户端
    return HttpResponse(html)

def render_views(request):
    return render(request,'01-temp.html')

def sayHi():
    return 'hello'

class Animal(object):
    name = '日尼玛'
    def eat(self):
        return 'eat'+self.name

def var_views(request):
    str = '这是模板中的字符串'
    num = 3306
    tup = ('西游记','水浒传','三国演义','红楼梦')
    list = [ '白骨精', '潘金莲', '赵云', '贾宝玉']
    dic = {
        'BJ':'北京',
        'SZ':'深圳',
        'SH':'上海',
    }
    dog = Animal()
    ret = sayHi()
    return render(request,'01-temp.html',locals())