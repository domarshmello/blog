# 应用的数据模型。所有Django应用必须有一个models.py文件，但该文件可以为空。
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager  # 添加django-taggit提供的TaggableManager管理器到Post模型：


# Create your models here.

class BlogType(models.Model):
    type_name = models.CharField(verbose_name='分类', max_length=20)

    # 返回显示类别名称即可
    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField(verbose_name='标题', max_length=60)
    blog_type = models.ForeignKey(BlogType, verbose_name='类型', on_delete=models.DO_NOTHING)
    # content = models.TextField(verbose_name='内容')
    content = RichTextField(verbose_name='内容')
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    last_update_time = models.DateTimeField(verbose_name='更新时间', auto_now_add=True)
    tags = TaggableManager()  # tags器管理网求允许你从Blog对象中添加，检索和移除标签。
    readed_num = models.IntegerField(verbose_name='点击阅读量', default=0)

    # 其中%s是占位符，先占个位子，用%后面的内容替换。
    # __str__()方法是对象的默认可读表示
    # 这种写法是有利于看清完整的字符串结构。也可以写成 "<Blog:" + self.title + ">" 直接把字符串拼接起来，明显要麻烦很多。另外self.title是python类的用法，取当前类的title字段值。
    def __str__(self):
        return '<Blog: %s>' % self.title

    # 模型中的Meta类包含元数据。我们告诉Django，查询数据库时，默认排序是publish字段的�降序排列。我们使用负号前缀表示降序排列。
    class Meta:
        ordering = ['-created_time']
