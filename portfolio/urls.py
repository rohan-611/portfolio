from django.urls import path
from .views import *

app_name = 'portfolio'

urlpatterns = [
    path('portfolio/', Portfolios.as_view(), name='portfolio'),
    path('portfolio/<pk>', PortfolioDetailView.as_view(), name='portfolio_details'),
    path('research-and-publications/', ResearchAndPublicationsView.as_view(), name='randp'),
    path('research-and-publications/<pk>', RandpDetailView.as_view(), name='randp_details'),
]