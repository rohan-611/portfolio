from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    responded = models.BooleanField(default = 0, blank=True, null=True)

    def __str__(self):
        return self.subject
    

class Testimonial(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    display = models.BooleanField(default=1, blank=True, null=True)

    def __str__(self):
        return self.name    