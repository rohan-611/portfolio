from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Blog, Teachings, Categories

# Create your views here.

class Blogs(ListView):
    template_name = "blog.html"
    queryset = Blog.objects.filter(draft=0).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(Blogs, self).get_context_data(**kwargs)
        context['blogs'] = Blog.objects.filter(draft=0).order_by("-id")[:4]
        context['categories'] = Categories.objects.all()
        return context

def BlogCategory(request, catid):
    cat = Categories.objects.filter(id=catid)[0].id
    print(cat)
    blog_list = Blog.objects.filter(draft = 0, category = cat).order_by("-id")
    blogs = Blog.objects.filter(draft=0).order_by("-id")[:4]
    categories = Categories.objects.all()

    context = {
        'blogs': blogs,
        'blog_list': blog_list,
        'categories': categories
    }

    return render(request, "blog.html", context)

def BlogDetail(request, pk):
        blog = get_object_or_404(Blog, id=pk, draft=False)
        blog_content = blog.content.splitlines()
        blog_list = Blog.objects.filter().order_by("-id")[:4]
        category_list = Categories.objects.all()
        context = {
            'blog':blog,
            'blog_content': blog_content,
            'blogs': blog_list,
            'categories': category_list
        }
        
        return render(request, 'blog_details.html', context)

class Teachings(ListView):
    template_name = "teachings.html"
    queryset = Teachings.objects.filter(display=1).order_by('-id')