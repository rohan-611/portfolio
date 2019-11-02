from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)

class About(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category

class Portfolio(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    picture = models.ImageField(upload_to='project_images', default='default.png', blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now=False, blank=True, null=True)
    display = models.BooleanField(default = 0, blank=True, null=True)

    def __str__(self):
        return self.title
    

class ResearchAndPublication(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    display = models.BooleanField(default = 0, blank=True, null=True)

    def __str__(self):
        return self.title