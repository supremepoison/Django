from django.conf.urls import url
from .views import *

urlpatterns = [
    #当访问路径为 index/ 的时候,则将请求交个index_views使徒处理函数去处理
    #完完整的请求路径为 http://localhost:8000/music/index
    url(r'^index/$',index_views),
    #当访问路径为空的时候,则将请求交给index_views去处理
    url(r'^$', index_views),

]