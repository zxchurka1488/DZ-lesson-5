from django.shortcuts import render
from django.http import HttpResponse

def index_0(request):
    return 0
def index_DZ_4(request):
    return HttpResponse(request, '<h1>Домашка по 4 занятию</h1>')