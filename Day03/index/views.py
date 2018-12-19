from django.db.models import Avg, Sum, Count
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def addbook_views(request):
    #方式1: Entry.object.create()
    # book = Book.objects.create(title='Python',publicate_date='2015-10-12')
    # print('新增加的数据的ID为%d'% book.id)

    #方式2: 通过entry创建对象,对象.save()
    # book = Book(title='database')
    # book.publicate_date='2013-01-21'
    # book.save()
    # print('新增加的数据的ID为%d'% book.id)

    # Book.objects.create(title='Web',publicate_date='2018-01-15')
    # Book.objects.create(title='AI',publicate_date='2015-02-15')
    # Book.objects.create(title='Advanced Web Development',publicate_date='2015-10-15')
    # Book.objects.create(title='Python Web Programming',publicate_date='2017-03-23')

    Author.objects.create(name='xixi',age=22,email='111qqqq@qq.com')
    Author.objects.create(name='heihei',age=23,email='wang111qqqq@qq.com')
    Author.objects.create(name='haha',age=33,email='21qqqq@qq.com')
    Author.objects.create(name='王尼玛',age=53,email='111wang@qq.com')



    return HttpResponse('Add book successfully')



def query_views(request):
    #1.基本查询操作 - all()
    # books = Book.objects.all()
    # print(type(books))
    # for i in books:
    #     print('ID:%d' % i.id)
    # print(books.query)

    # #2.查询返回部分列
    # books = Book.objects.values('title','publicate_date')
    # for book in books:
    #     print('name:%s,publicate_date:%s' % (book['title'],book['publicate_date']))

    #3.查询返回指定列
    # books = Book.objects.values_list('title', 'publicate_date')
    # for i in books:
    #     print('name:%s,publicate_date:%s' % (i[0],i[1]))

    #4.查询只返回一条数据 - get()
    # book = Book.objects.get(id=1)
    # print(book.title)

    #5.查询id为1的book的信息
    # list= Book.objects.filter(id=1)
    # print(list)

    #6.查询publicate_date为2018-01-15的Book的信息
    # list = Book.objects.filter(publicate_date = '2018-01-15')
    # print(list)
    # for i in list:
    #     print('ID:%d,title:%s,publicate_date:%s' % (i.id,i.title,i.publicate_date))

    #7.查询 id 为1 并且 publicate_date 为2015-10-12
    # list = Book.objects.filter(publicate_date='2015-10-12', id=1)
    # print(list)
    # for i in list:
    #     print('ID:%d,title:%s,publicate_date:%s' % (i.id, i.title, i.publicate_date))

    #8.查询 publicate_date是2015的所有数据
    # list= Book.objects.filter(publicate_date__year__gt=2015)
    # for i in list:
    #     print('ID:%d,title:%s,publicate_date:%s' % (i.id, i.title, i.publicate_date))

    #9.练习

    #1.查询Author表中age大于等于30的AUthor信息
    # at = Author.objects.filter(age__gt=30)

    #2.查询Author表中所有姓'王'的Author信息
    # at = Author.objects.filter(name__contains='王')

    #3.查询Author表中Email中包含'wang'的Author的信息
    # at = Author.objects.filter(email__contains='wang')

    #4.查询Author表中age大于'RapWang'的age的所有的信息
    # at = Author.objects.filter(age__gt=(Author.objects.get(name='RapWang').age))
    #
    # for i in at:
    #     print(i.id,i.name,i.age,i.email)


    #10.查询Author表中根据age升序排序
    # result = Author.objects.order_by('age')
    # for i in result:
    #     print(i.id,i.name,i.age,i.email)

    #11.查询Author表中所有人的平均年龄 - 聚合函数aggregate()
    # result = Author.objects.aggregate(avg=Avg('age'))
    # print(result)

    #12. 查询Book表中每个时间日期所发行书的数量
    # result= Book.objects.values('publicate_date').annotate(count=Count('title')).values('publicate_date','count').all()
    # print(result)

    list = Book.objects.filter(id__gt=1).values('publicate_date').annotate(count=Count('title')).filter(count__gt=1).values('publicate_date','count').all()
    print(list)
    return HttpResponse('<script>alert("NB")</script>')