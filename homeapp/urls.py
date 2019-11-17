from django.urls import path
import homeapp.views as views

app_name = 'homeapp'

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
]
