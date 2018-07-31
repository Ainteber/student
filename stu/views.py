import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from stu.models import Student, StudentInfo, Class

logger = logging.getLogger('stu')


def index(request):

    if request.method == 'GET':
        stuinfos = StudentInfo.objects.all()
        logger.info('url: %s method:%s 获取学生信息成功' % (request.path, request.method))
        return render(request, 'index.html', {'stuinfos': stuinfos})


def addStu(request):
    if request.method == 'GET':
        return render(request, 'addStu.html')

    if request.method == 'POST':
        name = request.POST.get('name')
        num = request.POST.get('num')

        stu = Student.objects.create(
            stu_name=name,
            stu_num=num
        )
        return redirect(
            reverse('s:addinfo', kwargs={'stu_id': stu.id})
        )


def addStuInfo(request, stu_id):

    if request.method == 'GET':

        return render(request, 'addStuInfo.html', {'stu_id':stu_id})

    if request.method == 'POST':

        stu_id = request.POST.get('stu_id')

        # 添加头像图片
        img = request.FILES.get('img')

        StudentInfo.objects.create(s_id=stu_id, i_image=img)

        return HttpResponseRedirect('/stu/index/')


def addClass(request):

    if request.method == 'GET':

        return render(request, 'addClass.html')

    if request.method == 'POST':

        name = request.POST.get('name')
        num = request.POST.get('num')
        clas = request.POST.get('clas')

        Student.objects.create(
            s_name=name,
            s_num=num,
            s_class=clas
            )
        Class.objects.create(s_class=clas,
                             s_name=name,
                             s_num=num)
        return HttpResponseRedirect('/stu/index/')


def addGrade(request):

    if request.method == 'GET':

        return render(request, 'addGrade.html')

    if request.method == 'POST':

        s_num = request.POST.get('num')
        s_name = request.POST.get('name')
        s_sex = request.POST.get('sex')
        s_Chinese = request.POST.get('Chinses')
        s_Math = request.POST.get('Math')
        s_English = request.POST.get('English')

        StudentInfo.objects.create(s_num=s_num,
                                   s_name=s_name,
                                   s_sex=s_sex,
                                   s_Chinese=s_Chinese,
                                   s_Math=s_Math,
                                   s_English=s_English)

        return HttpResponseRedirect('/stu/index/')


def selectStu(request):
    stus = Student.objects.all()

    if request.method == 'POST':
        s_name = request.POST.get('stuname')
        stus = Student.objects.filter(stu_name=s_name)
        return render(request, 'sel_stut.html', {'stus': stus})

    return render(request, 'sel_stu.html', {'stus': stus})
