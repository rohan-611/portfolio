from django.db import models
from django.utils.text import slugify
from image_cropping import ImageRatioField

COUNTRY_CODES = [
    ('+91', 'INDIA')
]


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(max_length=300, blank=True, null=True)
    about_me = models.TextField(max_length=300, blank=True, null=True)
    country_code = models.CharField(max_length=4, choices=COUNTRY_CODES, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    phone_timings = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=40, blank=True, null=True)
    email_timings = models.CharField(max_length=50, blank=True, null=True)
    experience_years = models.IntegerField(blank=True, null=True)
    linked_in = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    stack_overflow = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True, upload_to='profile/')
    cv = models.FileField(upload_to='resume/', null=True, blank=True)

    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return str(self.user)


class Publication(models.Model):
    user = models.ForeignKey(Profile, related_name='publications', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=140, blank=True, null=True)
    url = models.URLField(verbose_name='pub_url', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    authors = models.CharField(max_length=150, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if len(self.slug) > 50:
                self.slug = self.slug[:50]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, related_name='testimonials')
    offering_from = models.CharField(max_length=25, blank=True, null=True)
    text = models.CharField(max_length=150, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    linked_in = models.URLField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True, upload_to='testimonial/')
    cropped_photo = ImageRatioField('photo', '75x75')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.text.endswith('"'):
            self.text = f'"{self.text}"'
        super().save()

    def __str__(self):
        return f'Testimonial from: {self.offering_from}'
