# Generated by Django 2.1.4 on 2018-12-20 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_author_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
