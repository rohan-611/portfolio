from django.contrib import admin
from image_cropping import ImageCroppingMixin

from homeapp import models


class TestimonialAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(models.Profile)
admin.site.register(models.Publication)
admin.site.register(models.Testimonial, TestimonialAdmin)
