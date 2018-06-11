from json import dumps
from django.core.paginator import Paginator
from django.db.models import F, Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from app.filters import StudentFilter
from app.models import Grade, Student
from app.serializer import StudentSerializer, GradeSerializer
from day010.settings import PAGE_NUMBERS
from rest_framework import mixins, viewsets

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def left(request):
    if request.method == 'GET':
        return render(request, 'left.html')


def grade(request):
    if request.method == 'GET':
        page_num = request.GET.get('page_num', 1)
        grades = Grade.objects.all()
        """分页处理,每页3个"""
        paginator = Paginator(grades, PAGE_NUMBERS)
        pages = paginator.page(int(page_num))
        return render(request, 'grade.html', {'grades': grades, 'pages': pages})


def head(request):
    if request.method == 'GET':
        return render(request, 'head.html')


def student(request):
    if request.method == 'GET':
        page_num = request.GET.get('page_num', 1)
        students = Student.objects.all().filter(delete=False)
        paginator = Paginator(students, PAGE_NUMBERS)
        pages = paginator.page(int(page_num))
        return render(request, 'student.html', {'students': students, 'pages': pages})
        # return render(request, 'student.html')

def addgrade(request):
    if request.method == 'GET':
        return render(request, 'addgrade.html')

    if request.method == 'POST':
        grade_name = request.POST['grade_name']
        Grade.objects.create(g_name=grade_name).save()
        return HttpResponseRedirect(reverse('grade'))


def addstu(request):
    if request.method == 'GET':
        grades = Grade.objects.all()
        return render(request, 'addstu.html', {'grades': grades})

    if request.method == 'POST':
        stu_name = request.POST['stu_name']
        grade_id = request.POST['select_id']
        s_img = request.FILES.get('s_img')
        Student.objects.create(s_name=stu_name, g_id=grade_id, s_img=s_img)
        return HttpResponseRedirect(reverse('student'))

"""
def del_stu(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    ctx = {'code': 200}
    return HttpResponse(dumps(ctx), content_type='application/json; charset=utf-8')
"""

def editgrade(request):
    if request.method == 'GET':
        g_id = request.GET.get('g_id')
        return render(request, 'addgrade.html', {'g_id': g_id})

    else:
        g_id = request.POST.get('g_id')
        grade_name = request.POST.get('grade_name')
        g = Grade.objects.filter(pk=g_id).first()
        g.g_name = grade_name
        g.save()

        return HttpResponseRedirect(reverse('grade'))


def select(request):

    grade = Grade.objects.filter(g_name='python')[0]
    students = grade.student_set.all()

    # 查询python班语文大于等于数学10分的学生
    # stu = students.filter(s_chinese__gte=F('s_math') + 10)    # F 计算的时候用

    #查询python班语文大于等于80或者数学小于等于80的学生
    # stu = students.filter(Q(s_chinese__gte=80) | Q(s_math__lte=80))  # Q 用于筛选 |或者 &而且 ~取反
    # for i in stu:
    #     print(i.id)

    # 查询python班语文大于等于80或者数学小于等于80的学生
    # stu = students.filter(~Q(s_chinese__gte=80) | Q(s_math__lte=80))
    # for i in stu:
    #     print(i.id)


class api_grade(mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                viewsets.GenericViewSet
                ):
    queryset = Grade.objects.all()

    serializer_class = GradeSerializer


class api_student(mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):

    #学生的所有信息
    queryset = Student.objects.all().filter(delete=False)
    #序列化学生的所有信息
    serializer_class = StudentSerializer
    #过滤
    filter_class = StudentFilter


    #重枸get请求的方法
    def get_queryset(self):

        query = self.queryset
        # #http://127.0.0.1:8000/app/api/student/?s_name=张
        # s_name = self.request.query_params.get('s_name')
        # s_chinese = self.request.query_params.get('s_chinese')
        # return query.filter(s_name__contains=s_name, s_chinese__gte=s_chinese)

        return query


    #重枸delete的请求的时候的方法
    def perform_destroy(self, instance):
        instance.delete = True
        instance.save()


def editgradebyapi(request):
    if request.method == 'GET':

        return render(request, 'addgrade.html')




