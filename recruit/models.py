from django.db import models
from django.utils import timezone


class Student(models.Model):
    phone_num = models.CharField(max_length=11, null=False, unique=True)
    name = models.CharField(max_length=20, null=False)
    school = models.CharField(max_length=30, null=False)
    stu_class = models.IntegerField(null=True, blank=True)
    stu_num = models.IntegerField(null=True, blank=True)
    per_uuid = models.UUIDField(null=False, unique=True)
    file_2 = models.CharField(max_length=100, null=True)
    file_1 = models.CharField(max_length=100, null=True)
    file_3 = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(default=timezone.now(), null=False)

    def __str__(self):
        return self.phone_num


class Authentication(models.Model):
    phone_num = models.CharField(max_length=11, null=False)
    code = models.IntegerField(null=False)
    supply = models.BooleanField(default=False, null=False)
    created_at = models.DateTimeField(default=timezone.now(), null=False)   # TODO: Check default time setting

    def __str__(self):
        return self.phone_num
