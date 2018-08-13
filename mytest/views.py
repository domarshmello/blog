from django.shortcuts import render, get_object_or_404

from django.shortcuts import render_to_response

# Create your views here.
from mytest.models import Blog, BlogType


def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render_to_response('blog_list.html', context)


def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, id=blog_pk)
    return render_to_response("blog_detail.html", context)


def blog_with_type(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    return render_to_response("blog_with_type.html", context)
