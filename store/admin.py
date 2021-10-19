from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from . import models

# 参考文档：https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/admin/#modeladmin-options

class InventoryFilter(admin.SimpleListFilter):
    title = "inventory"
    parameter_name = "inventory" #地址栏显示

    def lookups(self, request, model_admin): #what item should appears here
        return [
            ("<10", "Low price") #<10是逻辑 Low是现实的内容(人读的东西)
        ]
    
    def queryset(self, request, queryset):
        if self.value() == "<10": # self.value() return the selected filter
            return queryset.filter(inventory__lt=10)



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin): #这个class是product类的admin model
    actions = ["clear_inventory"]
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price"]
    list_filter = ["collection", "last_update", InventoryFilter]
    list_per_page = 30
    list_select_related = ["collection"]

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering="inventory") # django不知道怎么排序， 我们加一个decorator来说明应该按照inventory的多少来进行排序
    def inventory_status(self, product):
        if product.inventory < 10:
            return "Low"
        return "OK"

    @admin.action(description="Clear inventory")
    def clear_inventory(self, request, queryset): #request是用户的请求， queryset是选中的那些product
        updated_count = queryset.update(inventory=0)
        self.message_user(request, f'{updated_count} products were successfully updated', messages.ERROR) #展示给用户的信息 

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    ordering = ["first_name", "last_name" ] # 先按照fist_name 升序排序
    list_per_page = 30
    search_fields = ["first_name__istartwith", "last_name_istartwith"] # 搜索框 搜索cat: first_name或者last_name中有cat的


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "products_count"] # products_count是computed field

    @admin.display(ordering="products_count")
    def products_count(self, collection):
        url = (
            reverse("admin:store_product_changelist") #可以使用 Django 的 URL 反查系统 访问该网站提供的视图。
            + "?"
            + urlencode({"collection__id": str(collection.id)})) #原始的url是：/admin/store/product/?collection__id=1 相当于一个filter
        return format_html('<a href="{}">{}</a>', url, collection.products_count) # 这里<a>外面要使用单引号 原因: f-string大括号内所用的引号不能和大括号外的引号定界符冲突，可根据情况灵活切换 ' 和 "：若 ' 和 " 不足以满足要求，还可以使用 ''' 和 """：
        

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count("product")
        ) 


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer"]