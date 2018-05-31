from json import dumps
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from app.models import Grade, Student
from day010.settings import PAGE_NUMBERS


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
        students = Student.objects.all()
        paginator = Paginator(students, PAGE_NUMBERS)
        pages = paginator.page(int(page_num))
        return render(request, 'student.html', {'students': students, 'pages': pages})


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


def del_stu(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    ctx = {'code': 200}
    return HttpResponse(dumps(ctx), content_type='application/json; charset=utf-8')


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



