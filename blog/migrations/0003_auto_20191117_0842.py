# Generated by Django 2.2.5 on 2019-11-17 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='homeapp.Profile'),
        ),
        migrations.AlterField(
            model_name='article',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='post/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
