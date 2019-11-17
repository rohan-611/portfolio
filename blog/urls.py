from django.urls import path

import blog.views as blog_view

app_name = 'blog'

urlpatterns = [
    path('', blog_view.BlogView.as_view(), name='blog_view'),
    path('category/<str:blog_name>', blog_view.BlogView.as_view(), name='blog_category_view'),
    path('category/<str:blog_name>/article/<slug:slug>', blog_view.ArticleDetailView.as_view(),
         name='article_details_url')
]
