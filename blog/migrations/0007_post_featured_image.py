# Generated by Django 4.2.18 on 2025-01-28 21:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_comment_email_remove_comment_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
