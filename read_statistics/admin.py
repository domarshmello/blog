from django.contrib import admin
from read_statistics.models import ReadNum


# Register your models here.

# ReadNum模型的管理器
@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'content_object')
