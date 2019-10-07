from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    responded = models.BooleanField(default = 0)

    def __str__(self):
        return self.subject
    

class Testimonials(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    content = models.TextField()
    display = models.BooleanField(default=1)

    def __str__(self):
        return self.name    