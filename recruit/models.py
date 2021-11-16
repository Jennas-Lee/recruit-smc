from django.db import models

from score.models import Score


class Document(models.Model):
    docu_integrated = models.CharField(null=False, max_length=100)
    interview = models.JSONField(null=False)
    # cert_web = models.CharField(null=True, blank=True, max_length=100)
    cert_online = models.CharField(null=True, blank=True, max_length=100)
    cert_offline = models.CharField(null=True, blank=True, max_length=100)
    cert_license = models.CharField(null=True, blank=True, max_length=100)
    cert_contest = models.CharField(null=True, blank=True, max_length=100)

    created_at = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self):
        return self.pk


class Student(models.Model):
    name = models.CharField(null=False, max_length=5)
    neis_number = models.CharField(null=True, blank=True, max_length=8, unique=True)
    first_major = models.CharField(null=False, max_length=1)
    second_major = models.CharField(null=False, max_length=1, default='0')
    school = models.CharField(null=False, max_length=30)
    grade = models.CharField(null=True, blank=True, max_length=1)
    Class = models.CharField(null=True, blank=True, max_length=2)
    number = models.CharField(null=True, blank=True, max_length=2)
    tel_st = models.CharField(null=False, unique=True, max_length=11)
    tel_pa = models.CharField(null=False, max_length=11)
    password = models.CharField(null=False, max_length=4)

    created_at = models.DateTimeField(null=False, auto_now_add=True)

    document = models.OneToOneField(Document, on_delete=models.CASCADE, related_name='document_pk', null=True,
                                    blank=True)
    score = models.OneToOneField(Score, on_delete=models.CASCADE, related_name='score_pk', null=True, blank=True)

    def __str__(self):
        return self.name
