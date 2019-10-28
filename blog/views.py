from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog, Teaching, Category

# Create your views here.

class Blogs(ListView):
    template_name = "blog/blog.html"
    queryset = Blog.objects.filter(draft=0).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(Blogs, self).get_context_data(**kwargs)
        context['blogs'] = Blog.objects.filter(draft=0).order_by("-id")[:4]
        context['categories'] = Category.objects.all()
        return context

def BlogCategory(request, catid):
    cat = Categories.objects.filter(id=catid)[0].id
    blog_list = Blog.objects.filter(draft = 0, category = cat).order_by("-id")
    blogs = Blog.objects.filter(draft=0).order_by("-id")[:4]
    categories = Category.objects.all()

    context = {
        'blogs': blogs,
        'blog_list': blog_list,
        'categories': categories
    }

    return render(request, "blog/blog.html", context)
    
class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_details.html"

class Teachings(ListView):
    template_name = "blog/teachings.html"
    queryset = Teaching.objects.filter(display=1).order_by('-id')