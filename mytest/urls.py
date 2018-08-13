from django.urls import path
from .views import blog_detail, blog_list, blog_with_type

urlpatterns = [
    # localhost:8000/article/
    path('', blog_list, name="blog_list"),
    # localhost:8000/article/1
    path('detail/<int:blog_pk>', blog_detail, name="blog_detail"),
    path('type/<int:blog_type_pk>', blog_with_type, name="blog_with_type"),
]
