from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from portfolio.models import *
from blog.models import Blog

# Create your views here.

class Portfolios(ListView):
    template_name = "portfolio.html"
    queryset = Portfolio.objects.filter(display=1).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(Portfolios, self).get_context_data(**kwargs)
        context['project_categories'] = Categories.objects.all()
        return context

def PortfolioDetail(request, pk):
    portfolio = get_object_or_404(Portfolio, id=pk, display=1)
    portfolio_desc = portfolio.desc.splitlines()
    portfolio_details = portfolio.details.splitlines()

    context = {
        'portfolio': portfolio,
        'portfolio_desc' : portfolio_desc,
        'portfolio_details' : portfolio_details
    }

    return render(request, 'portfolio-details.html', context)

class Profile(TemplateView):
    template_name = "profile.html"