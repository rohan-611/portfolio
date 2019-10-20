from django.db import models

# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length = 50)

    def __str__(self):
        return self.category


class Blog(models.Model):
    title = models.CharField(max_length=256)
    picture = models.ImageField(upload_to='blog_pictures', default='default.jpg')
    category = models.ForeignKey(Categories, blank=True, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateField()
    draft = models.BooleanField(default=0)

    def __str__(self):
        return self.title

class Teachings(models.Model):

    title = models.CharField( max_length=50)
    content = models.TextField()
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.content

class Comments(models.Model):
    blog = models.ForeignKey(Blog , on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    comment = models.TextField()
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)

    def __str__(self):
        return self.comment


class Replies(models.Model):
    comment_id = models.ForeignKey(Comments, on_delete=models.CASCADE)
    user = models.TextField()
    comment = models.TextField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.comment
