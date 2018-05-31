from django.db import models


class CarRecord(models.Model):
    carno = models.CharField(max_length=7, verbose_name='车牌号')
    reason = models.CharField(max_length=50, verbose_name='违章原因')
    date = models.DateTimeField(db_column='happen_date', auto_now_add=True, verbose_name='违章时间')
    punish = models.CharField(max_length=50, verbose_name='处罚方式')
    isdone = models.BooleanField(default=False, verbose_name='是否受理')

    @property
    def happen_date(self):
        return self.date.strftime('%Y-%m-%d %H:%M:%S')
        """
        return '%d年%02d月%02d日 %02d:%02d:%02d' % \
               (self.date.year, self.date.month, self.date.day,
                self.date.hour, self.date.minute, self.date.second)
        """

    class Meta:
        db_table = 'tb_car_record'
        ordering = ('-date', )
