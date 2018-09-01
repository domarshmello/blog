from django.contrib.sitemaps import Sitemap
from mytest.models import Blog
from django.urls import reverse


class MySiteMap(Sitemap):
    changefreq = 'daily'  # 可选,指定每个对象的更新频率
    priority = 0.6  # 可选,指定每个对象的优先级,默认0.5

    def items(self):  # 返回对象的列表.这些对象将被其他方法或属性调用
        return Blog.objects.all()

    def lastmod(self, obj):  # 可选,该方法返回一个datetime,表示每个对象的最后修改时间
        return obj.last_update_time

    def location(self, obj):  # 可选.返回每个对象的绝对路径.如果对象有get_absolute_url()方法,可以省略location
        return reverse('blog', kwargs={'blog_id': obj.id})





