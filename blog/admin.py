from django.contrib import admin
from image_cropping import ImageCroppingMixin
from import_export.admin import ImportExportModelAdmin

import blog.models as models


class BlogAdmin(ImageCroppingMixin, ImportExportModelAdmin):
    class Meta:
        model = models.Blog


class ArticleAdmin(ImageCroppingMixin, ImportExportModelAdmin):
    class Meta:
        model = models.Article


admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Article, ArticleAdmin)
