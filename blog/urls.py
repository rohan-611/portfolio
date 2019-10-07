from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('blogs/', Blogs.as_view(), name='blogs'),
    path('blogs/<catid>/', BlogCategory, name='blogcategory'),
    path('teachings/', Teachings.as_view(), name='teachings'),
    path('blogs/blog-details/<pk>/', BlogDetail, name='blog_detail'),
]
