from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Products...')


def new(request):
    return HttpResponse('New Products.')



