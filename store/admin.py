from django.contrib import admin
from . import models

# 参考文档：https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/admin/#modeladmin-options
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin): #这个class是product类的admin model
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price"]
    list_per_page = 30
    list_select_related = ["collection"]

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering="inventory") # django不知道怎么排序， 我们加一个decorator来说明应该按照inventory的多少来进行排序
    def inventory_status(self, product):
        if product.inventory < 10:
            return "Low"
        return "OK"

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    ordering = ["first_name", "last_name" ] # 先按照fist_name 升序排序
    list_per_page = 30

admin.site.register(models.Collection)


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer"]