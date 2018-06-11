from django.db import models

# Create your models here.


# 创建班级的模型
class Grade(models.Model):
    g_id = models.AutoField(primary_key=True)
    g_name = models.CharField(max_length=20)
    g_create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'grade'


# 创建学生的模型：
class Student(models.Model):
    s_name = models.CharField(max_length=20, null=False, unique=True)
    s_img = models.ImageField(upload_to='upload', null=True)
    s_chinese = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    s_math = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    s_create_time = models.DateTimeField(auto_now_add=True)
    s_operate_time = models.DateTimeField(auto_now_add=True)
    delete = models.BooleanField(default=0)
    g = models.ForeignKey(Grade, on_delete=models.CASCADE)

    class Meta:
        db_table = 'student'


# 创建学生拓展的模型：
class StuInfo(models.Model):

    stu_addr = models.CharField(max_length=30)
    stu_age = models.IntegerField()
    stu = models.OneToOneField(Student, on_delete=models.CASCADE)

    class Meta:
        db_table = 'stu_info'