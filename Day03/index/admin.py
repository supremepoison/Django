from django.contrib import admin
from .models import *

#声明 Author 的高级管理类 AuthorAdmin
class AuthorAdmin(admin.ModelAdmin):
    #1.定义在列表页上显示的属性们
    list_display = ['name','age','email']
    #2.允许被点击的字段
    list_display_links = ['name','age']
    #3.允许被修改的字段
    list_editable = ['email']
    #4.添加允许被搜索的字段们
    search_fields = ['name','email']
    #5右侧添加过滤器
    list_filter = ['name','email']
    #7.指定在详情页中显示的字段以及排列的顺序
    # fields = ['name','email','age']
    #8.指定在详情页中的字段分组们
    fieldsets = (
        #分组1 : name,age
        ('基本选项',{
            'fields':('name','age'),
        }),
        #分组2 : email,isActive
        ('高级选项',{
            'fields':('email','active'),
            'classes':('collapse',),
        })
    )


class BookAdmin(admin.ModelAdmin):
    list_display = ['title','publicate_date']
    #6.顶部增加时间选择器
    date_hierarchy = 'publicate_date'


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name','address','city']
    list_editable = ['address','city']
    search_fields = ['city','address','name','website']
    fieldsets = (
        ('基本选项',{
            'fields':('name','address','city'),
        }),
        ('高级选项',{
            'fields':('country','website'),
            'classes':('collapse',),
        })

    )

# Register your models here.
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Wife)