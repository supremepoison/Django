# Generated by Django 2.1.4 on 2018-12-20 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20181220_0643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'wife',
            },
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-age'], 'verbose_name': 'author尼玛', 'verbose_name_plural': 'author尼玛'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-publicate_date'], 'verbose_name_plural': '书籍'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name_plural': '出版社'},
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=30, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publicate_date',
            field=models.DateField(verbose_name='发行时间'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=30, verbose_name='书名'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.CharField(max_length=200, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='city',
            field=models.CharField(max_length=30, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='country',
            field=models.CharField(max_length=30, verbose_name='国家'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=30, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='website',
            field=models.URLField(verbose_name='网站'),
        ),
        migrations.AddField(
            model_name='wife',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='index.Author'),
        ),
    ]
