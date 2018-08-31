from django.contrib import admin
from .models import Article


# Register your models here.

# admin.site.register(Article)

# 装饰器  修饰admin定制类
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "create_time", "is_delete",  "last_update_time", "content",  "readed_num")
    #  ,  代表元组 -倒序
    ordering = ("id",)
    # ordering = ("-id",)

# @admin.register(Article)代替下面的写法p
# admin.site.register(Article, ArticleAdmin)
