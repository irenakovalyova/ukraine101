# Generated by Django 4.0.3 on 2022-04-13 09:33

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='color',
            field=colorfield.fields.ColorField(choices=[('#FFFFFF', 'grey'), ('#000000', 'blue'), ('#000000', 'green'), ('#000000', 'orange'), ('#000000', 'purple'), ('#000000', 'red')], default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
    ]