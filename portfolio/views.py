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

class ResearchAndPublicationsView(ListView):
    model = ResearchAndPublications
    context_object_name = 'randp'
    template_name = "randp.html"


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

def ResearchAndPublicationsDetails(request, pk):
    randp = get_object_or_404(ResearchAndPublications, id=pk, display=1)
    randp_desc = randp.desc.splitlines()
    randp_details = randp.details.splitlines()

    context = {
        'randp': randp,
        'randp_desc' : randp_desc,
        'randp_details' : randp_details
    }

    return render(request, 'randp-details.html', context)