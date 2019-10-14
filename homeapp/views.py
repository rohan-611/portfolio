from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from blog.models import Blog, Teachings
from portfolio.models import Portfolio, Categories, Profile, About
from homeapp.models import Testimonials, Contact

# Create your views here

class Index(TemplateView):
    template_name = "homeapp/index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.all()[0]
        context['blog_list'] = Blog.objects.filter(draft=0).order_by("-date")[:3]
        context['teachings_list'] = Teachings.objects.filter(display=1)[:4]
        context['portfolio_list'] = Portfolio.objects.filter(display=1)[:6]
        context['category_list'] = Categories.objects.all()
        context['testimonials_list'] = Testimonials.objects.filter(display=1)
        return context

def ContactView(request):

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        contact = Contact()
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()

        return redirect("/")
    
    return render(request, "homeapp/contact.html")

class AboutView(TemplateView):
    template_name = "homeapp/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['about_list'] = About.objects.all()
        context['testimonials_list'] = Testimonials.objects.filter(display=1)
        return context