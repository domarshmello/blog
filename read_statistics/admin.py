from django.contrib import admin
from read_statistics.models import ReadNum, ReadDetail


# Register your models here.

# ReadNum模型的管理器
@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'content_object')


# ReadNum模型的管理器
@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display = ('date', 'read_num', 'content_object')
