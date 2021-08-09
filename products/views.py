from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello World')


def greet(request):
    return HttpResponse("Hi Bay! How are you doing?")
