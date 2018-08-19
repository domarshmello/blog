from django.contrib import admin
from .models import BlogType, Blog


# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


# Blog模型的管理器
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'title', 'blog_type', 'content', 'author', 'created_time', 'last_update_time')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-created_time',)

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'title')
    # 筛选器
    # list_filter = ('tags', 'created_time')  # 过滤器
    search_fields = ('title',)  # 搜索字段
    date_hierarchy = 'last_update_time'  # 详细时间分层筛选
