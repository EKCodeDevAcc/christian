from django.shortcuts import render

from .models import Product
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):

    return render(request, 'webapp/index.html')


# https://docs.djangoproject.com/en/3.1/topics/http/views/
def product_detail(request, product_id):
    try:

        # info of a product of the product_id
        item = Product.objects.get(product_id=product_id)

    except Product.DoesNotExist:

        # throw 404 with the error message
        raise Http404("Item does not exist.")

    return render(request, 'webapp/detail.html',
                { 'item': item })
