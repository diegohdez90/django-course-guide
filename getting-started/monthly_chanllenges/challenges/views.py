from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest):
    return HttpResponse('It works')
