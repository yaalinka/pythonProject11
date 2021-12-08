# Generated by Django 3.2.9 on 2021-12-06 19:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_alter_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, max_length=25, unique=True),
        ),
    ]
