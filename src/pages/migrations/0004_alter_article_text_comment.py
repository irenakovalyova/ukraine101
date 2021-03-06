# Generated by Django 4.0.3 on 2022-03-28 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0003_article_featured_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=djrichtextfield.models.RichTextField(),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(max_length=500)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
