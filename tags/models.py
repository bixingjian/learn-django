from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# tag的种类
class Tag(models.Model): 
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # what tag referring to what object 
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) # ContentType 就是一个虚拟类 上面需要导入
    object_id = models.PositiveIntegerField() # 这个object的id
    content_object = GenericForeignKey() # 真实的product,真是的object