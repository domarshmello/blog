# 用于存放应用的逻辑。每个视图接收一个HTTP请求，然后处理请求，并返回响应。
# 一个Django视图就是一个Python函数，它接收一个web请求，并返回一个web响应。视图中的所有逻辑返回期望的响应。

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
# 引入分页器
from django.core.paginator import Paginator
from mytest.models import Blog, BlogType
# Create your views here.


from taggit.models import Tag


# 视图接收request对象作为唯一的参数。记住，该参数是所有视图都必需的
def blog_list(request):
    blogs_all_list = Blog.objects.all()
    paginator = Paginator(blogs_all_list, 10)  # 每10篇分页
    page_num = request.GET.get('page', 1)  # 获取url的页面参数
    page_of_blogs = paginator.get_page(page_num)

    context = {}
    # 页面通过blogs对象可以获取数据
    # context['blogs'] = Blog.objects.all()
    # 属性object_list 返回具体的博客页面
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
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
    context['blog_type'] = blog_type
    # 筛选出特定的分类下的博客 模型定义的blog_type=查找到的类型
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)

    # 列表页面需要的blog_types 分类类型对象
    context['blog_types'] = BlogType.objects.all()
    return render_to_response("blog_with_type.html", context)
