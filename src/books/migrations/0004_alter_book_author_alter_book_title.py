# Generated by Django 4.0.3 on 2022-03-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_book_image_alter_book_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
