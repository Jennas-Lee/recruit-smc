from django.db import models


class Student(models.Model):
    name = models.CharField(null=False, max_length=5)
    school = models.CharField(null=False, max_length=21)
    grade = models.CharField(null=True, blank=True, max_length=1)
    _class = models.CharField(null=True, blank=True, max_length=2)
    number = models.CharField(null=True, blank=True, max_length=2)
    tel_st = models.CharField(null=False, unique=True, max_length=11)
    tel_pa = models.CharField(null=False, max_length=11)
    password = models.CharField(null=False, max_length=4)
    created_at = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    docu_integrated = models.CharField(null=False, max_length=100)
    cert_web = models.CharField(null=True, blank=True, max_length=100)
    cert_online = models.CharField(null=True, blank=True, max_length=100)
    cert_offline = models.CharField(null=True, blank=True, max_length=100)
    cert_license = models.CharField(null=True, blank=True, max_length=100)
    cert_contest = models.CharField(null=True, blank=True, max_length=100)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_id')

    def __str__(self):
        return self.student_id
