# Generated by Django 2.1.4 on 2018-12-21 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_book_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='publishe_set',
            field=models.ManyToManyField(to='index.Publisher'),
        ),
    ]