from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    designation = models.CharField(max_length=100)
    bachelors = models.CharField(max_length=150)
    masters = models.CharField(max_length=150)
    phd = models.CharField(max_length=150)
    bio = models.TextField()

class Categories(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Portfolio(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='project_images', default='default.png')
    desc = models.TextField()
    details = models.TextField()
    date = models.DateField(auto_now=False)
    display = models.BooleanField(default = 0)

    def __str__(self):
        return self.title
    

class ResearchAndPublications(models.Model):
    title = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='researchandpublications',default='default.png')
    desc = models.TextField()
    details = models.TextField()
    date = models.DateField()
    display = models.BooleanField(default = 0)


    def __str__(self):
        return self.title    