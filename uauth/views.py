from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from uauth.models import Users


def regist(request):

    if request.method == 'GET':

        return render(request, '_regist.html')

    if request.method == 'POST':
        # 注册
        name = request.POST.get('name')
        password = request.POST.get('password')
        password = make_password(password)

        Users.objects.create(u_name=name,
                             u_password=password)
        return HttpResponseRedirect('/uauth/login/')


def login(request):

    if request.method == 'GET':

        return render(request, '_login.html')

    if request.method == 'POST':

        name = request.POST.get('name')
        password = request.POST.get('password')

        if Users.objects.filter(u_name=name).exists():
            user = Users.objects.get(u_name=name)
            if check_password(password, user.u_password):
                response = HttpResponseRedirect('/stu/addstu/')
                return response
            else:
                return render(request, '_login.html', {'password': '用户密码错误'})
        else:
            return render(request, '_login.html', {'name': '用户不存在'})
