from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from portfolio.models import *
from blog.models import Blog

# Create your views here.

class Portfolios(ListView):
    template_name = "portfolio/portfolio.html"
    queryset = Portfolio.objects.filter(display=1).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(Portfolios, self).get_context_data(**kwargs)
        context['project_categories'] = Category.objects.all()
        return context

class ResearchAndPublicationsView(ListView):
    model = ResearchAndPublication
    context_object_name = 'randp'
    template_name = "portfolio/randp.html"

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = "portfolio/portfolio-details.html"

class RandpDetailView(DetailView):
    model = ResearchAndPublication
    template_name = "portfolio/randp-details.html"