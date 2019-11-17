from django.db import models

from blog.models import Category

COUNTRY_CODES = [
    ('+91', 'INDIA')
]


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField('auth.User', blank=True, null=True, on_delete=models.CASCADE, related_name='profile')
    designation = models.CharField(max_length=100, blank=True, null=True)
    bachelors = models.CharField(max_length=150, blank=True, null=True)
    masters = models.CharField(max_length=150, blank=True, null=True)
    phd = models.CharField(max_length=150, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    about_me = models.TextField(max_length=300, blank=True, null=True)
    country_code = models.CharField(max_length=4, choices=COUNTRY_CODES, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    phone_timings = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=40, blank=True, null=True)
    experience_years = models.IntegerField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    stack_overflow = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True, upload_to='profile/')
    cv = models.FileField(upload_to='resume/', null=True, blank=True)

    def __str__(self):
        return str(self.user) + '_profile'


class About(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    picture = models.ImageField(upload_to='project_images', default='default.png', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now=False, blank=True, null=True)
    display = models.BooleanField(default=0, blank=True, null=True)

    def __str__(self):
        return self.title


class ResearchAndPublication(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    display = models.BooleanField(default=0, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
