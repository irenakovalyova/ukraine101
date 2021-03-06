# Generated by Django 4.0.3 on 2022-03-28 12:33

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_image_alter_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='title'),
            preserve_default=False,
        ),
    ]
