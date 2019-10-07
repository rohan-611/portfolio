from django.urls import path
from .views import *

app_name = 'portfolio'

urlpatterns = [
    path('portfolio/', Portfolios.as_view(), name='portfolio'),
    path('portfolio/<pk>', PortfolioDetail, name='portfolio_details'),
    path('about/', Profile.as_view(), name='about'),
]