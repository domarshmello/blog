"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

from blog.sitemaps import MySiteMap
from . import views

# from django.contrib.sitemaps import sitemap    # 导入sitemap视图

sitemaps = {
    'blog': MySiteMap,
}

# url 列表 1.0版本使用的是url 2.0版本使用的是path
# 地址 and 第二个参数是请求的方法
urlpatterns = [
    # 首页   别名是home
    path('', views.home, name='home'),
    # 后台管理页面
    path('admin/', admin.site.urls),
    path('article/', include('article.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('blog/', include('mytest.urls')),
    # path('sitemap.xml', views.index, {'sitemaps': {'blog': BlogSitemap()}}),

    # path('sitemap-<section>.xml', views.sitemap, {'sitemaps': {'blog': BlogSitemap()}},
    #      name='django.contrib.sitemaps.views.sitemap'),
    # path('article/<int:article_id>', article_detail, name="article_detail"),
    # path('article/', article_list, name="article_list"),
]

# 设置media的访问路径
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



