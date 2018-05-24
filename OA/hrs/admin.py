from django.contrib import admin

# Register your models here.
from hrs.models import Dept, Emp


class DeptAdmin(admin.ModelAdmin):
    # 横向展示
    list_display = ('dno', 'name', 'location')
    #-no 为降序
    search_fields = ('name', 'location')
    ordering = ('dno', )


class EmpAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'job', 'sal', 'mar', 'dept')
    #添加搜索栏
    search_fields = ('name', 'job')
    # 排序
    ordering = ('dept', )


# 将表格同步到admin页面
admin.site.register(Dept, DeptAdmin)
admin.site.register(Emp, EmpAdmin)