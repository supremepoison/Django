"""day01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from .views import *

dic = {
    'name':'wangwc',
    'age':18,
}
urlpatterns = [
    url(r'^login/', admin.site.urls),
    url(r'^show/(\d{4})/$',show1_views),
    # url(r'sh',sh_views),
    url(r'^show/$',show_views),
    url(r'^show/(\d{4})/(\d{2})/(\d{2})/$',show2_views),
    #当访问路径为 /show3/的时候
    url(r'^show3/$',show3_views,dic)


]
