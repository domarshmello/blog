# 创建的文件
from django.http import HttpResponse
from django.shortcuts import render_to_response


#
# def index(request):
#     return HttpResponse("Hello world")

def home(request):
    context = {}
    return render_to_response('home.html', context)
