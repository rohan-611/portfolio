from django.contrib import admin
from .models import *

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'author']

    class Meta:
        modal = Blog

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']

    class Meta:
        modal = Categories
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Teachings)
admin.site.register(Comments)
admin.site.register(Replies)