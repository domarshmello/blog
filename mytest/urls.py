
from django.urls import path
from .views import blog_detail, blog_list

urlpatterns = [
    # localhost:8000/article/
    path('', blog_list, name="blog_list"),
    # localhost:8000/article/1
    path('blog/<int:blog_pk>', blog_detail, name="blog_detail"),
]