from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Blog, Teachings

# Create your views here.

class Blogs(ListView):
    template_name = "blog.html"
    queryset = Blog.objects.filter(draft=0).order_by('-date')
    
class Teachings(ListView):
    template_name = "teachings.html"
    queryset = Teachings.objects.filter(display=1).order_by('-id')

def BlogDetail(request, pk):
        blog = get_object_or_404(Blog, id=pk, draft=False)
        blog_content = blog.content.splitlines()
        context = {
            'blog':blog,
            'blog_content': blog_content,
        }
        return render(request, 'blog_details.html', context)