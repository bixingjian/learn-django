from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def say_hello(request):
    query_set = Product.objects.all()
    
    for product in query_set[:5]:
        print(product)
    return render(request, 'hello.html', {'name': 'Mosh'})
