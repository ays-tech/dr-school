# Generated by Django 4.1.7 on 2023-04-05 11:40

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=False, max_length=255, null=True, quality=100, scale=None, size=[800, 450], upload_to='post_images', verbose_name='Image (16:9)'),
        ),
    ]
