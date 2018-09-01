from django.urls import path
from .views import blog_detail, blog_list, blogs_with_type, blogs_with_date


urlpatterns = [
    # localhost:8000/article/
    path('', blog_list, name="blog_list"),
    # localhost:8000/article/1  防止都是数字
    path('detail/<int:blog_pk>', blog_detail, name="blog_detail"),
    path('type/<int:blog_type_pk>', blogs_with_type, name="blog_with_type"),
    path('date/<int:year>/<int:month>', blogs_with_date, name="blogs_with_date"),

]
