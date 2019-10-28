from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length = 50, blank=True, null=True)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name_plural = 'Categories'


class Blog(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True)
    picture = models.ImageField(upload_to='blog_pictures', default='default.jpg', blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    draft = models.BooleanField(default=0, blank=True, null=True)

    def __str__(self):
        return self.title

class Teaching(models.Model):

    title = models.CharField( max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    display = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.content

class Comment(models.Model):
    blog = models.ForeignKey(Blog , on_delete=models.CASCADE, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now=False, blank=True, null=True)
    time = models.TimeField(auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.comment


class Reply(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    user = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now=True, blank=True, null=True)
    time = models.TimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural = 'replies'
