from django.shortcuts import render
from django.views.generic import TemplateView

from blog.models import Blog, Teachings
from portfolio.models import Portfolio, Categories
from homeapp.models import Testimonials

# Create your views here

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['blog_list'] = Blog.objects.filter(draft=0).order_by("-date")[:3]
        context['teachings_list'] = Teachings.objects.filter(display=1)[:4]
        context['portfolio_list'] = Portfolio.objects.filter(display=1)[:6]
        context['category_list'] = Categories.objects.all()
        context['testimonials_list'] = Testimonials.objects.filter(display=1)
        return context

class Achievements(TemplateView):
    template_name = "achievements.html"

class Contact(TemplateView):
    template_name = "contact.html"

class About(TemplateView):
    template_name = "about.html"