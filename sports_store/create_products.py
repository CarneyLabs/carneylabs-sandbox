from django.db import transaction

import json

from sports_store.models import Product

import os


def create_products():
    path = os.path.abspath(os.path.join(os.path.pardir, 'products.json'))

    with open(name=path, mode='rt') as product_list:
        product_list_string = product_list.read()

    product_list_json = json.loads(unicode(product_list_string,'ISO-8859-1'))

    for product in product_list_json:
        with transaction.atomic():
            Product.objects.create(
                name=product['name'],
                description=product['description'],
                category=product['category'],
                price=product['price']
            )

if __name__ == '__main__':
    create_products()