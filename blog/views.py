# 创建的文件
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world")


