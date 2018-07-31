from django.conf.urls import url

from stu import views


urlpatterns = [
    url(r'addstu/', views.addStu),
    url(r'^addstuInfo/(?P<stu_id>\d+)/', views.addStuInfo, name='addinfo'),
    url('addClass/', views.addClass),
    url('addGrade/', views.addGrade),
    url(r'selectstu/', views.selectStu),
    url(r'^index/', views.index),
]