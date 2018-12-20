from django.db import models

# Create your models here.

#创建一个实体类 - Publisher 表示'出版社'
            #1.name: 出版社名称- varchar
            #2.address: 出版社地址 - varchar
            #3.city: 出版社所在城市 - varchar
            #4.country: 出版社所在国家 - varchar
            #5.website: 出版社网址- varchar


class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    address = models.CharField(max_length=200,verbose_name='地址')
    city = models.CharField(max_length=30,verbose_name='城市')
    country = models.CharField(max_length=30,verbose_name='国家')
    website = models.URLField(verbose_name='网站')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publisher'
        verbose_name_plural='出版社'


class Author(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True)
    active = models.BooleanField(default=True)

    #重写 __str__函数,以便定义对象在后台的表现名称
    def __str__(self):
        return self.name

    class Meta:
        #1.指定表名
        db_table = 'author'
        #2.指定在admin中显示的名称
        verbose_name='author尼玛'
        #3.指定在admin中显示的名称
        verbose_name_plural=verbose_name
        #4.指定在admin中按照年龄降序排序
        ordering=['-age']


class Book(models.Model):
    title = models.CharField(max_length=30,verbose_name='书名')
    publicate_date = models.DateField(verbose_name='发行时间')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
        verbose_name_plural='书籍'
        ordering=['-publicate_date']


class Wife(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    #增加对Author的一对一关联属性
    author = models.OneToOneField(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'wife'



