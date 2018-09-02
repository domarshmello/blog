# 创建的文件
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import render_to_response
from mytest.models import Blog
from read_statistics.utils import get_seven_days_read_data


def index(request):
    context = {}
    return render_to_response('sitemap.xml', context)


def home(request):
    # 获取blog类型
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)


    context = {}
    # 将阅读量写到对象read_nums
    context['read_nums'] = read_nums
    return render_to_response('home.html', context)
