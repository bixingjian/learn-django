from django.core import exceptions
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Count, Avg, Sum, Max, Min
from store.models import Product, Customer, OrderItem, Order


def say_hello(request):
    # queryset = Product.objects.all()[3:5]
    # queryset = Product.objects.filter(unit_price__range=(20,30))
    # queryset = Product.objects.filter(inventory__lt=10)
    # queryset = Customer.objects.filter(email__icontains=".com")

    # queryset = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20))

    # queryset = Product.objects.filter(inventory=F("collection__id"))

    # queryset = Product.objects.order_by("unit_price", "-title").reverse() # 默认是升序 "-"是降序
    # product = Product.objects.order_by("unit_price")[0]
    # product = Product.objects.earliest("unit_price")

    # res_dict = Product.objects.values("title", "unit_price", "collection__title") #value不回将所有的字段都返回，只返回指定的字段
    # res_tuple = Product.objects.values_list("title", "unit_price", "collection__title") #value不回将所有的字段都返回，只返回指定的字段
    
    # queryset = Product.objects.filter(id__in=OrderItem.objects.values("product_id").distinct()).order_by("title")

    # queryset = Product.objects.only("id", "title") # only会得到instace(真实的product), value只是返回dict. 谨慎使用, 可能会出现很慢的情况
    # queryset = Product.objects.defer("description") # defer不要一些字段, 谨慎使用

    # queryset = Product.objects.select_related("collection").all() #如果另一端的是一个(另一端是外键). product对应一个collection, collection可以有多个product
    # queryset = Product.objects.prefetch_related("promotions").all() #如果另一端是多个(manytomany, 外键的多的那一端) 
    # queryset = Product.objects.prefetch_related("promotions").select_related("collection").all() #preload的操作可以串在一起, 顺序没有要求
    queryset = Order.objects.select_related("customer").prefetch_related("orderitem_set__product").order_by("-placed_at")[:5]


    return render(request, 'hello.html', {'name': 'Mosh', "orders": queryset})
