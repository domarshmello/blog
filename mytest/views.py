# # 用于存放应用的逻辑。每个视图接收一个HTTP请求，然后处理请求，并返回响应。
# # 一个Django视图就是一个Python函数，它接收一个web请求，并返回一个web响应。视图中的所有逻辑返回期望的响应。
#
# from django.shortcuts import render, get_object_or_404
# from django.shortcuts import render_to_response
# # 引入分页器
# from django.core.paginator import Paginator
# from mytest.models import Blog, BlogType
# # Create your views here.
# from django.conf import settings
# from taggit.models import Tag
#
#
# # 视图接收request对象作为唯一的参数。记住，该参数是所有视图都必需的
# def blog_list(request):
#     blogs_all_list = Blog.objects.all()
#     # paginator = Paginator(blogs_all_list, 10)  # 每10篇分页
#     paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)
#     page_num = request.GET.get('page', 1)  # 获取url的页面参数
#     page_of_blogs = paginator.get_page(page_num)
#     current_page_num = page_of_blogs.number  # 获取当前页码
#     # page_range = [current_page_num - 2,  current_page_num - 1, current_page_num, current_page_num + 1,
#     # current_page_num + 2]
#
#     print(list(range(max(current_page_num - 2, 1), current_page_num)))
#
#     # 使用range()函数 max()和1进行比较 总页码数paginator.num_pages  ---->获取当前页面前后各两页的页码范围
#     page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
#                  list(range(current_page_num + 1, min(current_page_num + 2, paginator.num_pages + 1)))
#
#     # 加上省略页码标记 页码差 2 以上 。。。
#     if page_range[0] - 1 >= 2:
#         page_range.insert(0, '...')
#     # 如果第一个不是第一页 插入1页码
#     if page_range[0] != 1:
#         page_range.insert(0, 1)
#     # 加上省略页码标记 页码差 2 以上 。。。
#     if paginator.num_pages - page_range[-1] - 1 >= 2:
#         page_range.append('...')
#     # 如果第一个不是最后一页 插入最后总共的分的页码
#     if page_range[-1] != paginator.num_pages:
#         page_range.append(paginator.num_pages)
#
#     context = {}
#     # 页面通过blogs对象可以获取数据
#     # context['blogs'] = Blog.objects.all()
#     # 属性object_list 返回具体的博客页面
#     context['blogs'] = page_of_blogs.object_list
#     context['page_of_blogs'] = page_of_blogs
#     context['blog_types'] = BlogType.objects.all()
#     context['blog_dates'] = Blog.objects.dates('created_time', 'month', order='DESC')
#     # context['blog_count'] = Blog.objects.all().count()
#     tag = None
#     return render_to_response('blog_list.html', context)
#
#
# def blog_with_type(request, blog_type_pk):
#     context = {}
#     # 得到类型 pk=传入进来的变量 blog_type_pk =====urls里的参数blog_type_pk
#     blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
#
#     context['blog_type'] = blog_type
#
#     # 筛选出特定的分类下的博客 模型定义的blog_type=查找到的类型
#     context['blogs'] = Blog.objects.filter(blog_type=blog_type)
#
#     # 列表页面需要的blog_types 分类类型对象
#     context['blog_types'] = BlogType.objects.all()
#     return render_to_response("blog_with_type.html", context)
#
#
#
# # 按照日期  年 月 分类
# def blogs_with_date(request, year, month):
#     context = {}
#     blogs_all_list = Blog.objects.filter(created_time__year=year, created_time__month=month)
#
#     paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)
#     page_num = request.GET.get('page', 1)  # 获取url的页面参数
#     page_of_blogs = paginator.get_page(page_num)
#     current_page_num = page_of_blogs.number  # 获取当前页码
#     # page_range = [current_page_num - 2,  current_page_num - 1, current_page_num, current_page_num + 1,
#     # current_page_num + 2]
#
#     print(list(range(max(current_page_num - 2, 1), current_page_num)))
#
#     # 使用range()函数 max()和1进行比较 总页码数paginator.num_pages  ---->获取当前页面前后各两页的页码范围
#     page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
#                  list(range(current_page_num + 1, min(current_page_num + 2, paginator.num_pages + 1)))
#
#     # 加上省略页码标记 页码差 2 以上 。。。
#     if page_range[0] - 1 >= 2:
#         page_range.insert(0, '...')
#     # 如果第一个不是第一页 插入1页码
#     if page_range[0] != 1:
#         page_range.insert(0, 1)
#     # 加上省略页码标记 页码差 2 以上 。。。
#     if paginator.num_pages - page_range[-1] - 1 >= 2:
#         page_range.append('...')
#     # 如果第一个不是最后一页 插入最后总共的分的页码
#     if page_range[-1] != paginator.num_pages:
#         page_range.append(paginator.num_pages)
#
#     context['blogs'] = page_of_blogs.object_list
#     context['page_of_blogs'] = page_of_blogs
#     context['page_range'] = page_range
#     context['blog_type'] = BlogType.objects.all()
#     context['blogs_with_date'] = Blog.objects.dates ('created_time', 'month', order="DESC")
#     context['blogs_with_date'] = '%s年%s月' % (year, month)
#     return render_to_response('blogs_with_date.html', context)
#
#
#
# def blog_detail(request, blog_pk):
#     context = {}
#     blog = get_object_or_404(Blog, pk=blog_pk)
#
#     # 不考虑按照id取 是因为可能删除之后的blog  不好操作
#     context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
#     context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
#     context['blog'] = blog
#     # if not request.COOKIES.get('blog_%s_readed' % blog_pk):
#     #     blog.readed_num += 1
#     #     blog.save()
#     # context['blog'] = get_object_or_404(Blog, pk=blog_pk)
#     # context['blog'] = get_object_or_404(Blog, id=blog_pk)
#
#     # response = render_to_response('blog/blog_detail.html', context)  # 响应
#     # response.set_cookie('blog_%s_readed' % blog_pk, 'true')
#     # return response
#     return render_to_response("blog_detail.html", context)
#

from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count
from .models import Blog, BlogType

from read_statistics.utils import read_statistics_once_read


def get_blog_list_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)
    page_num = request.GET.get('page', 1)  # 获取url的页面参数（GET请求）
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number  # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    # 获取博客分类的对应博客数量
    # blog_types = BlogType.objects.all()
    # blog_types_list = []
    # for blog_type in blog_types:
    #     # 参数名blog_type = 参数值 blog_type
    #     blog_type.blog_count = Blog.objetcs.filter(blog_type=blog_type).count()
    #     blog_types_list.append(blog_type)

    # 获取日期归档对应的博客数量
    blog_dates = Blog.objects.dates('created_time', 'month', order="DESC")
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year,
                                         created_time__month=blog_date.month).count()

        blog_dates_dict[blog_date] = blog_count

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))  # annotate拓展查询字段 blog是模型对象  统计?
    context['blog_dates'] = blog_dates_dict
    return context


def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request, blogs_all_list)
    return render_to_response('blog_list.html', context)


def blogs_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blog_type'] = blog_type
    return render_to_response('blog_with_type.html', context)


def blogs_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(created_time__year=year, created_time__month=month)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blogs_with_date'] = '%s年%s月' % (year, month)
    return render_to_response('blogs_with_date.html', context)


def blog_detail(request, blog_pk):
    # blog_pk===key
    blog = get_object_or_404(Blog, pk=blog_pk)

    read_cookie_key = read_statistics_once_read(request, blog)

    # 字典的get方法 获取key  不存在key的时候 ===代表刚打开浏览器    加1操作
    if not request.COOKIES.get('blog_%s_readed' % blog_pk):
        # 判断博客记录存在？
        # if ReadNum.objects.filter(blog=blog).count():
        #     readnum = ReadNum.objects.get(blog=blog)
        #     # readnum.read_num += 1
        #     # readnum.save()
        #
        #     # blog.readed_num += 1
        #     # blog.save()
        # else:
        #     #不存在对应的记录
        #     readnum = ReadNum()
        #     # readnum.read_num += 1
        #     # readnum.blog = blog
        # readnum.read_num += 1
        # readnum.save()
        pass

    context = {}
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['blog'] = blog
    response = render_to_response('blog_detail.html', context)  # 响应
    # 利用cookie  （在python中 是以字典的形式保存 ===使用保存key  ）来保存阅读点击量      response.set_cookie(key, value) 120s有效
    # max_age=120, expires=datetime 2选一 即可  不写的话 cookie就是关闭浏览器失效
    # response.set_cookie('blog_%s_readed' % blog_pk, 'true', max_age=120, expires=datetime)
    # response.set_cookie('blog_%s_readed' % blog_pk, 'true')
    response.set_cookie(read_cookie_key, 'true')  # 阅读cookie标记

    return response
