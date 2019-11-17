from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from homeapp.models import Profile
from image_cropping import ImageRatioField


class Blog(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    background_image = models.ImageField(blank=True, null=True, upload_to='blog/background')  # size 360 x 220
    cropping = ImageRatioField('background_image', '360x220')
    tag_line = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:blog_category_view', kwargs={'blog_name': self.name})


class Article(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1, related_name='articles')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True, related_name='articles')
    title = models.CharField(max_length=140, unique=True)
    background_image = models.ImageField(blank=True, null=True, upload_to='post/%Y/%m')
    cropping = ImageRatioField('background_image', '555x280')
    slug = models.SlugField(blank=True, null=True)
    short_description = models.CharField(max_length=150, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    publish_on = models.DateTimeField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_on']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if not len(self.slug) <= 50:
            self.slug = self.slug[:50]
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:article_details_url', kwargs={'blog_name': self.blog.name, 'slug': self.slug})

    def next_article(self):
        _next = Article.objects.filter(id__gt=self.id)
        if _next:
            return _next.first()
        return False

    def previous_article(self):
        _previous = Article.objects.filter(id__gt=self.id).order_by('-id')
        if _previous:
            return _previous.first()
        return False
