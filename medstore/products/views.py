from django.http import JsonResponse
from .models import Product
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def product_list(request):
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)