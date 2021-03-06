from django.db.models import Avg, Sum, Count, F, Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.

def addbook_views(request):
    # 方式1: Entry.object.create()
    # book = Book.objects.create(title='Python',publicate_date='2015-10-12')
    # print('新增加的数据的ID为%d'% book.id)

    # 方式2: 通过entry创建对象,对象.save()
    # book = Book(title='database')
    # book.publicate_date='2013-01-21'
    # book.save()
    # print('新增加的数据的ID为%d'% book.id)

    # Book.objects.create(title='Web',publicate_date='2018-01-15')
    # Book.objects.create(title='AI',publicate_date='2015-02-15')
    # Book.objects.create(title='Advanced Web Development',publicate_date='2015-10-15')
    # Book.objects.create(title='Python Web Programming',publicate_date='2017-03-23')

    Author.objects.create(name='xixi', age=22, email='111qqqq@qq.com')
    Author.objects.create(name='heihei', age=23, email='wang111qqqq@qq.com')
    Author.objects.create(name='haha', age=33, email='21qqqq@qq.com')
    Author.objects.create(name='王尼玛', age=53, email='111wang@qq.com')

    return HttpResponse('Add book successfully')


def query_views(request):
    # 1.基本查询操作 - all()
    # books = Book.objects.all()
    # print(type(books))
    # for i in books:
    #     print('ID:%d' % i.id)
    # print(books.query)

    # #2.查询返回部分列
    # books = Book.objects.values('title','publicate_date')
    # for book in books:
    #     print('name:%s,publicate_date:%s' % (book['title'],book['publicate_date']))

    # 3.查询返回指定列
    # books = Book.objects.values_list('title', 'publicate_date')
    # for i in books:
    #     print('name:%s,publicate_date:%s' % (i[0],i[1]))

    # 4.查询只返回一条数据 - get()
    # book = Book.objects.get(id=1)
    # print(book.title)

    # 5.查询id为1的book的信息
    # list= Book.objects.filter(id=1)
    # print(list)

    # 6.查询publicate_date为2018-01-15的Book的信息
    # list = Book.objects.filter(publicate_date = '2018-01-15')
    # print(list)
    # for i in list:
    #     print('ID:%d,title:%s,publicate_date:%s' % (i.id,i.title,i.publicate_date))

    # 7.查询 id 为1 并且 publicate_date 为2015-10-12
    # list = Book.objects.filter(publicate_date='2015-10-12', id=1)
    # print(list)
    # for i in list:
    #     print('ID:%d,title:%s,publicate_date:%s' % (i.id, i.title, i.publicate_date))

    # 8.查询 publicate_date是2015的所有数据
    # list= Book.objects.filter(publicate_date__year__gt=2015)
    # for i in list:
    #     print('ID:%d,title:%s,publicate_date:%s' % (i.id, i.title, i.publicate_date))

    # 9.练习

    # 1.查询Author表中age大于等于30的AUthor信息
    # at = Author.objects.filter(age__gt=30)

    # 2.查询Author表中所有姓'王'的Author信息
    # at = Author.objects.filter(name__contains='王')

    # 3.查询Author表中Email中包含'wang'的Author的信息
    # at = Author.objects.filter(email__contains='wang')

    # 4.查询Author表中age大于'RapWang'的age的所有的信息
    # at = Author.objects.filter(age__gt=(Author.objects.get(name='RapWang').age))
    #
    # for i in at:
    #     print(i.id,i.name,i.age,i.email)

    # 10.查询Author表中根据age升序排序
    # result = Author.objects.order_by('age')
    # for i in result:
    #     print(i.id,i.name,i.age,i.email)

    # 11.查询Author表中所有人的平均年龄 - 聚合函数aggregate()
    # result = Author.objects.aggregate(avg=Avg('age'))
    # print(result)

    # 12. 查询Book表中每个时间日期所发行书的数量
    # result= Book.objects.values('publicate_date').annotate(count=Count('title')).values('publicate_date','count').all()
    # print(result)

    list = Book.objects.filter(id__gt=1).values('publicate_date').annotate(count=Count('title')).filter(
        count__gt=1).values('publicate_date', 'count').all()
    print(list)
    return HttpResponse('<script>alert("NB")</script>')


def delete_views(request, id):
    author = Author.objects.filter(id=id)
    author.update(active=False)
    return redirect('/homework')


def homework(request):
    result = Author.objects.filter(active=True).all()
    return render(request, 'homework.html', locals())


def update_views(request):
    # author=Author.objects.get(id=1)
    # author.age=40
    # author.save()

    author = Author.objects.exclude(id=1)
    author.update(age=45)

    return HttpResponse('万万没想到 啦啦啦啦啦')


def F_views(request):
    Author.objects.all().update(age=F('age') + 10)
    return HttpResponse('Nice')


def doQ_views(request):
    authors = Author.objects.filter(Q(id=1) | Q(active=True))
    for au in authors:
        print('id:%d,name:%s' % (au.id, au.name))
    return HttpResponse(1)


def oto_views(request):
    # 声明 wife对象,并指定其author的信息
    # wife = Wife()
    # wife.name ='大夫人'
    # wife.age = 20
    # wife.author_id = 1
    # wife.save()

    # wife = Wife()
    # wife.name = 'Slut'
    # wife.age = 23
    # author = Author.objects.get(id=2)
    # wife.author=author
    # wife.save()

    # 查询 - 正向查询(通过wife查询author)
    # wife = Wife.objects.get(id=1)
    # author = wife.author
    # print(author)

    # 查询 - 反向查询(通过author查询wife)
    author = Author.objects.get(id=1)
    wife = author.wife
    print(wife)

    return HttpResponse('OtO ok ')


def otm_views(request):
    # 1.正向查询:通过Book查询Publisher
    book = Book.objects.get(id=1)
    publisher = book.publisher
    print(publisher.name)
    # 2.反向查询:通过Publisher查询Book
    pub = Publisher.objects.get(id=1)
    books = pub.book_set.all()
    print('出版社名称:'+pub.name)
    print('所出版的图书:')
    for book in books:
        print('Book Title:'+ book.title)

    return HttpResponse('很棒')

def mtm_views(request):
    #查询id为1的book的author
    book = Book.objects.get(id=1)
    print('书名:'+book)
    author = book.authors.all()
    for au in author:
        print('作者'+au.name)

