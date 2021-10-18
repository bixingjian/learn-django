from django.contrib.contenttypes.models import ContentType
from django.core import exceptions
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.fields import DecimalField
from django.db.models import Q, F, Value, Func, ExpressionWrapper
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Avg, Sum, Max, Min
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product, Customer, OrderItem, Order
from tags.models import TaggedItem, Tag


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
    # queryset = Order.objects.select_related("customer").prefetch_related("orderitem_set__product").order_by("-placed_at")[:5]

    # res_dict = Product.objects.filter(collection__id=1).aggregate(count=Count("id"), min_price=Min("unit_price"))
    # res_dict = Order.objects.filter(customer__id=1).aggregate(count=Count("id"))
    # res_dict = Product.objects.filter(collection__id=3).aggregate(min_price=Min("unit_price"), avg_price=Avg("unit_price"), max_price=Max("unit_price"))

    # queryset = Customer.objects.annotate(is_new=Value(True))
    # queryset = Customer.objects.annotate(new_id=F("id")+1)

    # queryset = Customer.objects.annotate(full_name=Func(F("first_name"), Value(" "), F("last_name"), function="concat"))
    # queryset = Customer.objects.annotate(full_name=Concat("first_name", Value(" "), "last_name"))

    # queryset = Customer.objects.annotate(orders_count=Count("order")) #使用order 不是 order_set

    # discounted_price = ExpressionWrapper(F("unit_price") * 0.8, output_field=DecimalField()) 
    # queryset = Product.objects.annotate(discounted_price = discounted_price)
    # queryset = Customer.objects.annotate(orders_count=Count("order")).filter(orders_count__gt=5)

    TaggedItem.objects.get_tags_for(Product, 1)


    return render(request, 'hello.html', {'name': 'Mosh', "tags": list(queryset)})
