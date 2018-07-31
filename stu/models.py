from django.db import models


class Student(models.Model):
    stu_name = models.CharField(max_length=6)
    stu_num = models.CharField(max_length=10, unique=True)
    stu_sex = models.BooleanField()

    class Meta:
        db_table = 'stu_student'


class StudentInfo(models.Model):

    i_image = models.ImageField(upload_to='upload', null=True)
    s = models.OneToOneField(Student)

    class Meta:
        db_table = 'stu_studentinfo'


class Class(models.Model):

    s_name = models.CharField(max_length=6)
    s_num = models.CharField(max_length=10, unique=True)
    s_class = models.CharField(max_length=15)

    class Meta:
        db_table = 'stu_class'


class Grade(models.Model):

    s_num = models.CharField(max_length=10, unique=True)
    s_name = models.CharField(max_length=6)
    s_Chinese = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    s_Math = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    s_English = models.DecimalField(max_digits=4, decimal_places=1, default=0)

    class Meta:
        db_table = 'stu_grade'