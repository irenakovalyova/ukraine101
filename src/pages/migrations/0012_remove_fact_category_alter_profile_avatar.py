# Generated by Django 4.0.3 on 2022-04-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fact',
            name='category',
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='img/profile-photos/'),
        ),
    ]
