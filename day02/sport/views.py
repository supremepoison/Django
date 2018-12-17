from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def sport_views(request):
    return HttpResponse('Sport-index')