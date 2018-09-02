from django.db import models
from django.db.models.fields import exceptions
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.


class ReadNum(models.Model):
    read_num = models.IntegerField(verbose_name='点击阅读量', default=0)

    # ContentType文档  1 ：FK对应记录模型  2：记录对应模型的pk值  ==object_id  数值类型 3：获取外键对应信息
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


# 找到对应的记录 返回 阅读量 or 返回0  self形参对应 传来的具体model名
class ReadNumExpandMethod:
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0
