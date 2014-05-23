from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import json

from sports_store.models import Order
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


@require_POST
@csrf_exempt
def orders(request):
    if len(request.body) > 0:
        body_json = json.loads(request.body)

        Order.objects.create(
            name=body_json['name'],
            street=body_json['street'],
            city=body_json['city'],
            state=body_json['state'],
            zip=body_json['zip'],
            country=body_json['country'],
            giftwrap=body_json['giftwrap'],
            products=body_json['products']
        )

    return HttpResponse(status=200)