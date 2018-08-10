from django.db import models
from django.utils import timezone


# Create your models here.

class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    author = models.CharField(verbose_name='作者', max_length=50)
    content = models.TextField(verbose_name='文章内容')
    # create_time = models.DateTimeField(default=timezone.now)
    create_time = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    last_update_time = models.DateTimeField(verbose_name='更新日期', auto_now=True)
    # author=models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    is_delete = models.BooleanField(verbose_name='删除', default=False)
    readed_num = models.IntegerField(default=0)
