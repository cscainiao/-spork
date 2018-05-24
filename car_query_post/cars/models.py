from django.db import models

# Create your models here.


class Car(models.Model):
    no = models.AutoField(primary_key=True, verbose_name='编号')
    plate_number = models.CharField(max_length=8, verbose_name='车牌号')
    date = models.DateField(verbose_name='违章日期')
    why = models.CharField(max_length=9999, verbose_name='违章原因')
    mode = models.CharField(max_length=100, verbose_name='处罚方式')
    accept = models.BooleanField(default=0, verbose_name='是否受理')

    class Meta:
        db_table = 'tb_cars'