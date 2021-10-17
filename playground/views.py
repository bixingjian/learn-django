from django.core import exceptions
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer


def say_hello(request):
    # queryset = Product.objects.filter(unit_price__range=(20,30))
    queryset = Product.objects.filter(inventory__lt=10)
    # queryset = Customer.objects.filter(email__icontains=".com")
    return render(request, 'hello.html', {'name': 'Mosh', "products": list(queryset)})
