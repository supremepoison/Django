# Generated by Django 2.1.4 on 2018-12-20 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_author_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='isActive',
        ),
        migrations.AlterModelTable(
            name='author',
            table='author',
        ),
    ]
