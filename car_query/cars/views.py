from datetime import datetime
from json import JSONEncoder

from django import forms
from django.http import JsonResponse
from django.shortcuts import render



# 序列化/串行化/腌咸菜 - 把对象按照某种方式处理成字节或者字符的序列
# 反序列化/反串行化 - 把字符或者字节的序列重新还原成对象
# Python实现序列化和反序列化的工具模块 - json / pickle / shelve
# return HttpResponse(json.dumps(obj), content_type='application/json')
# return JsonResponse(obj, encoder=, safe=False)
# from django.core.serializers import serialize
# return HttpResponse(serialize('json', obj), content_type='application/json; charset=utf-8')
from cars.models import CarRecord


class CarRecordEncoder(JSONEncoder):

    def default(self, o):
        del o.__dict__['_state']
        o.__dict__['date'] = o.happen_date
        return o.__dict__


def ajax_search(request):
    current_time = datetime.now().ctime()
    last_visit_time = request.COOKIES.get('last_visit_time')
    if request.method == 'GET':
        response = render(request,'search.html', {'last': last_visit_time if last_visit_time else '你是第一次访问我们网站'})
        response.set_cookie('last_visit_time', current_time, max_age=1029600) #如果有last_visit_time 就last_visit_time, 否则current_time,保留时间1029600s
        return response
    else:
        carno = request.POST['carno']
        record_list = list(CarRecord.objects.filter(carno__icontains=carno))
        # 第一个参数是要转换成JSON格式(序列化)的对象
        # encoder参数要指定完成自定义对象序列化的编码器(JSONEncoder的子类型)
        # safe参数的值如果为True那么传入的第一个参数只能是字典
        # return HttpResponse(json.dumps(record_list), content_type='application/json; charset=utf-8')
        return JsonResponse(record_list, encoder=CarRecordEncoder,
                            safe=False)


def search(request):
    # 请求行中的请求命令
    # print(request.method)
    # 请求行中的路径
    # print(request.path)
    # 请求头(以HTTP_打头的键是HTTP请求的请求头)
    # print(request.META)
    # 查询参数: http://host/path/resource?a=b&c=d
    # print(request.GET)
    # 表单参数
    # print(request.POST)
    if request.method == 'GET':
        ctx = {'show_result': False}
    else:
        carno = request.POST['carno']
        ctx = {
            'show_result': True,
            'record_list': list(CarRecord.objects.filter(carno__contains=carno))}
    return render(request, 'search.html', ctx)


class CarRecordForm(forms.ModelForm):
    carno = forms.CharField(min_length=7, max_length=7, label='车牌号', error_messages={'carno': '请输入有效的车牌号'})
    reason = forms.CharField(max_length=50, label='违章原因')
    punish = forms.CharField(max_length=50, required=False, label='处罚方式')


    class Meta:
        model = CarRecord
        fields = ('carno', 'reason', 'punish')
    """
    提供额外的表单验证
    def clean_carno(self):
        _carno = self.cleaned_data['carno']
        if not condition: 
            raise forms.ValidationError('')
        return carno
    """

def add(request):
    errors = []
    if request.method == 'GET':
        f = CarRecordForm()
    else:
        f = CarRecordForm(request.POST)
        if f.is_valid():
            f.save()
            f = CarRecordForm()
        else:
            errors = f.errors.values()
    return render(request, 'add.html', {'f': f, 'errors': errors})
