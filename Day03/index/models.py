from django.db import models

# Create your models here.

#创建一个实体类 - Publisher 表示'出版社'
            #1.name: 出版社名称- varchar
            #2.address: 出版社地址 - varchar
            #3.city: 出版社所在城市 - varchar
            #4.country: 出版社所在国家 - varchar
            #5.website: 出版社网址- varchar


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    website = models.URLField()


class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(null=True)

class Book(models.Model):
    title = models.CharField(max_length=30)
    publicate_date = models.DateField()