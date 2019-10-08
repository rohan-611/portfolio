from django.urls import path
from .views import *

app_name = 'homeapp'

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView, name='contact'),
]
