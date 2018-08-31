# 用于存放应用的逻辑。每个视图接收一个HTTP请求，然后处理请求，并返回响应。

# 一个Django视图就是一个Python函数，它接收一个web请求，并返回一个web响应。视图中的所有逻辑返回期望的响应。

from django.shortcuts import render, get_object_or_404

from django.shortcuts import render_to_response

# Create your views here.
from mytest.models import Blog, BlogType

from taggit.models import Tag


# 视图接收request对象作为唯一的参数。记住，该参数是所有视图都必需的
def blog_list(request):
    context = {}
    # 页面通过blogs对象可以获取数据

    context['blogs'] = Blog.objects.all()

    context['blog_types'] = BlogType.objects.all()
    # context['blog_count'] = Blog.objects.all().count()
    tag = None
    return render_to_response('blog_list.html', context)


def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    # context['blog'] = get_object_or_404(Blog, id=blog_pk)
    return render_to_response("blog_detail.html", context)


def blog_with_type(request, blog_type_pk):
    context = {}
    # 得到类型 pk=传入进来的变量 blog_type_pk =====urls里的参数blog_type_pk
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    # 筛选出特定的分类下的博客 模型定义的blog_type=查找到的类型
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
# 列表页面需要的blog_types
    context['blog_types'] = BlogType.objects.all()
    return render_to_response("blog_with_type.html", context)
