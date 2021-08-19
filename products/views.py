from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'index.html')


def products(request):
    get_products = Product.objects.all()
    return render(request, 'products.html',
                  {'products': get_products})


def new(request):
    return HttpResponse('New Products.')



