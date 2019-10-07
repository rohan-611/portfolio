from django.urls import path
from .views import *

app_name = 'homeapp'

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('achievements/', Achievements.as_view(), name='achievements'),
    path('contact/', Contact.as_view(), name='contact'),
    path('about/', About.as_view(), name='about'),
]
