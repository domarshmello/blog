from django.contrib.auth.models import User
from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class BlogType(models.Model):
    type_name = models.CharField(verbose_name='分类', max_length=20)

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField(verbose_name='标题', max_length=60)
    blog_type = models.ForeignKey(BlogType, verbose_name='类型', on_delete=models.DO_NOTHING)
    content = models.TextField(verbose_name='内容')
    # content = RichTextUploadingField(verbose_name='内容')
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    last_update_time = models.DateTimeField(verbose_name='更新时间', auto_now_add=True)

    # 其中%s是占位符，先占个位子，用%后面的内容替换。
    # 这种写法是有利于看清完整的字符串结构。也可以写成 "<Blog:" + self.title + ">" 直接把字符串拼接起来，明显要麻烦很多。另外self.title是python类的用法，取当前类的title字段值。
    def __str__(self):
        return '<Blog: %s>' % self.title
