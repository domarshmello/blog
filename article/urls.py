
from django.urls import path
from .views import article_detail, article_list

urlpatterns = [
    # localhost:8000/article/
    path('', article_list, name="article_list"),
    # localhost:8000/article/1
    path('article/<int:article_id>', article_detail, name="article_detail"),



]