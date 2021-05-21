from django.db import models


class StdUserTb(models.Model):
    IDX = models.AutoField(primary_key=True, null=False)
    USER_NM = models.CharField(max_length=5, null=False)
    USER_SCHOOL_NM = models.CharField(max_length=30, null=True, blank=True)
    USER_GRADE_NO = models.IntegerField(null=True, blank=True)
    USER_NUMBER_NO = models.IntegerField(null=True, blank=True)
    USER_STD_PHONE_CD = models.CharField(max_length=11, unique=True, null=True, blank=True)
    USER_PRT_PHONE_CD = models.CharField(max_length=11, null=True, blank=True)
    USER_ADDRESS_TXT = models.TextField(null=True, blank=True)

    USER_CREATED_YMD = models.DateTimeField(auto_now_add=True, null=False)
    USER_UPDATED_YMD = models.DateTimeField(auto_now=True, null=False)
    USER_DELETED_YMD = models.DateTimeField(null=True, blank=True)

    USER_RESP_TCR_USER_IDX = models.ForeignKey('TcrUserTb', related_name='TEACHER', on_delete=models.RESTRICT,
                                               db_column='USER_RESP_TCR_USER_IDX', null=True)

    def __str__(self):
        return self.USER_NM

    class Meta:
        db_table = u'STD_USER_TB'


class StdDocTb(models.Model):
    IDX = models.AutoField(primary_key=True, null=False)
    DOC_COVER = models.TextField(null=True, blank=True)
    DOC_PLAN = models.TextField(null=True, blank=True)
    DOC_CERT_WED = models.JSONField(null=True)
    DOC_CERT_ACA_ON = models.JSONField(null=True)
    DOC_CERT_ACA_OFF = models.JSONField(null=True)
    DOC_CERT_LIC = models.JSONField(null=True)
    DOC_CERT_CON = models.JSONField(null=True)
    DOC_CERT_POR = models.JSONField(null=True)

    DOC_CREATED_YMD = models.DateTimeField(auto_now_add=True, null=False)
    DOC_UPDATED_YMD = models.DateTimeField(auto_now=True, null=False)
    DOC_DELETED_YMD = models.DateTimeField(null=True, blank=True)

    DOC_STD_USER_IDX = models.ForeignKey('StdUserTb', related_name='STUDENT', on_delete=models.RESTRICT,
                                         db_column='DOC_STD_USER_IDX', null=True)

    def __str__(self):
        return self.IDX

    class Meta:
        db_table = u'STD_DOC_TB'


class StdRecruitTb(models.Model):
    IDX = models.AutoField(primary_key=True, null=False)
    STD_RECEIPT_NM = models.IntegerField(null=False, unique=True)
    STD_RECEIPT_TYPE_CD = models.IntegerField(null=False)
    STD_WANT_1ST_CD = models.IntegerField(null=False)
    STD_WANT_2ND_CD = models.IntegerField(null=True)
    STD_WANT_3RD_CD = models.IntegerField(null=True)
    STD_WANT_4TH_CD = models.IntegerField(null=True)
    STD_PASSWORD_CD = models.TextField(null=False)

    STD_CREATED_YMD = models.DateTimeField(auto_now_add=True, null=False)
    STD_UPDATED_YMD = models.DateTimeField(auto_now=True, null=False)
    STD_DELETED_YMD = models.DateTimeField(null=True, blank=True)

    STD_USER_IDX = models.ForeignKey('StdUserTb', related_name='STUDENT', on_delete=models.RESTRICT,
                                     db_column='STD_USER_IDX', null=True)
    STD_RESP_TCR_USER_IDX = models.ForeignKey('TcrUserTb', related_name='TEACHER', on_delete=models.RESTRICT,
                                              db_column='STD_RESP_TCR_USER_IDX', null=True)

    def __str__(self):
        return self.IDX

    class Meta:
        db_table = u'STD_RECRUIT_TB'


class TcrUserTb(models.Model):
    IDX = models.AutoField(primary_key=True, null=False)
    USER_NM = models.CharField(max_length=5, null=False)
    USER_ST = models.IntegerField(null=False)

    USER_CREATED_YMD = models.DateTimeField(auto_now_add=True, null=False)
    USER_UPDATED_YMD = models.DateTimeField(auto_now=True, null=False)
    USER_DELETED_YMD = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.USER_NM

    class Meta:
        db_table = u'TCR_USER_TB'


class ScoreTb(models.Model):
    IDX = models.AutoField(primary_key=True, null=False)
    SCORE_NM = models.IntegerField(null=False)
    SCORE_TYPE_CD = models.IntegerField(null=False)

    SCORE_CREATED_YMD = models.DateTimeField(auto_now_add=True, null=False)
    SCORE_UPDATED_YMD = models.DateTimeField(auto_now=True, null=False)
    SCORE_DELETED_YMD = models.DateTimeField(null=True, blank=True)

    STD_USER_IDX = models.ForeignKey('StdUserTb', related_name='STUDENT', on_delete=models.RESTRICT,
                                     db_column='STD_USER_IDX', null=True)
    TCR_USER_IDX = models.ForeignKey('TcrUserTb', related_name='TEACHER', on_delete=models.RESTRICT,
                                     db_column='TCR_USER_IDX', null=True)

    def __str__(self):
        return self.IDX

    class Meta:
        db_table = u'SCORE_TB'
