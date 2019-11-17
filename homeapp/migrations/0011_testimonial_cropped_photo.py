# Generated by Django 2.2.5 on 2019-11-17 18:33

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0010_testimonial_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='cropped_photo',
            field=image_cropping.fields.ImageRatioField('photo', '75x75', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropped photo'),
        ),
    ]
