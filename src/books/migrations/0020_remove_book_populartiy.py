# Generated by Django 4.0.3 on 2022-04-13 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_book_populartiy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='populartiy',
        ),
    ]
