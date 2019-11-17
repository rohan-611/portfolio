from django.views import generic as dv

from .models import Blog, Article


class BlogView(dv.ListView):
    template_name = 'blog/blog.html'
    model = Article
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data()
        ctx['blog_list'] = Blog.objects.all()
        return ctx

    def get_queryset(self):
        if self.kwargs.get('blog_name'):
            return self.queryset_if_blog_name_given()
        return self.queryset_if_no_blog_name_given()

    def queryset_if_blog_name_given(self):
        return self.model.objects.filter(blog__name=self.kwargs['blog_name'])

    def queryset_if_no_blog_name_given(self):
        return self.model.objects.all()


class ArticleDetailView(dv.DetailView):
    template_name = 'blog/article_detail.html'
    model = Article
