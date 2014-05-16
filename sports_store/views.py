from django.http import HttpResponse
from django.shortcuts import render

import json

from sports_store.models import Product


def home(request):
    return render(request, 'sports_store/home.html')


def products(request):
    products_list = [{
        'id': product.id,
        'name': product.name,
        'description':product.description,
        'category': product.category,
        'price': float(product.price)
    } for product in Product.objects.all()]

    products_json = json.dumps(products_list)

    return HttpResponse(content=products_json, content_type='application/json')