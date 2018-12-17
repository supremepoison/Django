from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/$',login_views),
    url(r'^register/$',register_views),
    url(r'^$',index_views),
    url(r'^01-temp/$',temp_views),
    url(r'^02-temp/$',render_views),
    url(r'^03-var/$',var_views)
]