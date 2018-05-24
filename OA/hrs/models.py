from django.db import models

# Create your models here.


class Dept(models.Model):
    dno = models.IntegerField(primary_key=True, verbose_name='部门编号')
    name = models.CharField(max_length=20, verbose_name='部门名称')  # db_column=  数据库中名字 db_index= 创建索引
    location = models.CharField(max_length=10, verbose_name='部门地点')
    excellent = models.BooleanField(default=0, verbose_name='是否优秀')

    def __str__(self):
        # 将页面emp里面显示的dept外键约束的部门编号显示为部门名称
        return self.name

    class Meta:
        # 将数据库中默认生成的表格名称修改
        db_table = 'tb_dept'


class Emp(models.Model):
    no = models.IntegerField(primary_key=True, verbose_name='员工编号')
    name = models.CharField(max_length=20, verbose_name='员工姓名')
    job = models.CharField(max_length=10, verbose_name='职位')
    mar = models.CharField(max_length=20, null=True,blank=True, verbose_name='主管')
    sal = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='工资')
    comm = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='补贴')
    dept = models.ForeignKey(Dept, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tb_emp'