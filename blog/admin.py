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
        modal = Category
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoriesAdmin)
admin.site.register(Teaching)
admin.site.register(Comment)
admin.site.register(Reply)