from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Article


# Create your views here.

# def article_detail(request, article_id):
#     return HttpResponse("文章id: %s" % article_id)

# 引用模型获取文章通过objects

# http://127.0.0.1:8000/article/1 前台测试  优化方案 2
# def article_detail(request, article_id):
#     try:
#         article=Article.objects.get(id=article_id)
#     except Article.DoesNotExit:
#         # return HttpResponse("文章不存在")
#         raise Http404("not exist")
#     return HttpResponse("<h2>文章标题：%s </h2><br>文章作者：%s <br>文章内容: %s" % (article.title,article.author,article.content))


# 处理数据
# def article_detail(request, article_id):
#     try:
#         article=Article.objects.get(id=article_id)
#     except Article.DoesNotExit:
#         return HttpResponse("文章不存在")
#         raise Http404("not exist")
#     def article_detail(request, article_id):
#         try:
#             article=Article.objects.get(id=article_id)
#             文章内容是一个字典的形式
#             context={}
#             context['article_obj'] = article
#             request 模板的地址 内容 两种方式
#             return render(request, "article_detail.html", context)
#             return render_to_response("article_detail.html", context)
#         except Article.DoesNotExit:
#             return HttpResponse("文章不存在")
#             raise Http404("not exist")

# 处理数据
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    # 文章内容是一个字典的形式
    context = {}
    context['article_obj'] = article
    return render_to_response("article_detail.html", context)


def article_list(request):
    articles = Article.objects.all()
    context = {}
    context['articles'] = articles
    return render_to_response("article_list.html", context)
