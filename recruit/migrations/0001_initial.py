# Generated by Django 3.2.2 on 2021-06-03 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TcrUserTb',
            fields=[
                ('IDX', models.AutoField(primary_key=True, serialize=False)),
                ('USER_ID_TXT', models.CharField(max_length=15, unique=True)),
                ('USER_PASSWORD_TXT', models.TextField()),
                ('USER_TEAM_CD', models.IntegerField()),
                ('USER_NM', models.CharField(max_length=5)),
                ('USER_ST', models.IntegerField()),
                ('USER_CREATED_YMD', models.DateTimeField(auto_now_add=True)),
                ('USER_UPDATED_YMD', models.DateTimeField(auto_now=True)),
                ('USER_DELETED_YMD', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'TCR_USER_TB',
            },
        ),
        migrations.CreateModel(
            name='StdUserTb',
            fields=[
                ('IDX', models.AutoField(primary_key=True, serialize=False)),
                ('USER_NM', models.CharField(max_length=5)),
                ('USER_SCHOOL_NM', models.CharField(blank=True, max_length=30, null=True)),
                ('USER_GRADE_NO', models.IntegerField(blank=True, null=True)),
                ('USER_NUMBER_NO', models.IntegerField(blank=True, null=True)),
                ('USER_STD_PHONE_CD', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('USER_PRT_PHONE_CD', models.CharField(blank=True, max_length=11, null=True)),
                ('USER_ADDRESS_TXT', models.TextField(blank=True, null=True)),
                ('USER_CREATED_YMD', models.DateTimeField(auto_now_add=True)),
                ('USER_UPDATED_YMD', models.DateTimeField(auto_now=True)),
                ('USER_DELETED_YMD', models.DateTimeField(blank=True, null=True)),
                ('USER_RESP_TCR_USER_IDX', models.ForeignKey(db_column='USER_RESP_TCR_USER_IDX', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='USER_RESP_TCR_USER', to='recruit.tcrusertb')),
            ],
            options={
                'db_table': 'STD_USER_TB',
            },
        ),
        migrations.CreateModel(
            name='StdRecruitTb',
            fields=[
                ('IDX', models.AutoField(primary_key=True, serialize=False)),
                ('STD_RECEIPT_NM', models.IntegerField(unique=True)),
                ('STD_RECEIPT_TYPE_CD', models.IntegerField()),
                ('STD_WANT_1ST_CD', models.IntegerField()),
                ('STD_WANT_2ND_CD', models.IntegerField(null=True)),
                ('STD_WANT_3RD_CD', models.IntegerField(null=True)),
                ('STD_WANT_4TH_CD', models.IntegerField(null=True)),
                ('STD_PASSWORD_CD', models.TextField()),
                ('STD_CREATED_YMD', models.DateTimeField(auto_now_add=True)),
                ('STD_UPDATED_YMD', models.DateTimeField(auto_now=True)),
                ('STD_DELETED_YMD', models.DateTimeField(blank=True, null=True)),
                ('STD_RESP_TCR_USER_IDX', models.ForeignKey(db_column='STD_RESP_TCR_USER_IDX', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='RECRUIT_TCR_USER', to='recruit.tcrusertb')),
                ('STD_USER_IDX', models.ForeignKey(db_column='STD_USER_IDX', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='RECRUIT_STD_USER', to='recruit.stdusertb')),
            ],
            options={
                'db_table': 'STD_RECRUIT_TB',
            },
        ),
        migrations.CreateModel(
            name='StdDocTb',
            fields=[
                ('IDX', models.AutoField(primary_key=True, serialize=False)),
                ('DOC_COVER', models.TextField(blank=True, null=True)),
                ('DOC_PLAN', models.TextField(blank=True, null=True)),
                ('DOC_CERT_WED', models.JSONField(null=True)),
                ('DOC_CERT_ACA_ON', models.JSONField(null=True)),
                ('DOC_CERT_ACA_OFF', models.JSONField(null=True)),
                ('DOC_CERT_LIC', models.JSONField(null=True)),
                ('DOC_CERT_CON', models.JSONField(null=True)),
                ('DOC_CERT_POR', models.JSONField(null=True)),
                ('DOC_CREATED_YMD', models.DateTimeField(auto_now_add=True)),
                ('DOC_UPDATED_YMD', models.DateTimeField(auto_now=True)),
                ('DOC_DELETED_YMD', models.DateTimeField(blank=True, null=True)),
                ('DOC_STD_USER_IDX', models.ForeignKey(db_column='DOC_STD_USER_IDX', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='DOC_STD_USER', to='recruit.stdusertb')),
            ],
            options={
                'db_table': 'STD_DOC_TB',
            },
        ),
        migrations.CreateModel(
            name='ScoreTb',
            fields=[
                ('IDX', models.AutoField(primary_key=True, serialize=False)),
                ('SCORE_NM', models.IntegerField()),
                ('SCORE_TYPE_CD', models.IntegerField()),
                ('SCORE_CREATED_YMD', models.DateTimeField(auto_now_add=True)),
                ('SCORE_UPDATED_YMD', models.DateTimeField(auto_now=True)),
                ('SCORE_DELETED_YMD', models.DateTimeField(blank=True, null=True)),
                ('STD_USER_IDX', models.ForeignKey(db_column='STD_USER_IDX', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='SCORE_STD_USER', to='recruit.stdusertb')),
                ('TCR_USER_IDX', models.ForeignKey(db_column='TCR_USER_IDX', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='SCORE_TCR_USER', to='recruit.tcrusertb')),
            ],
            options={
                'db_table': 'SCORE_TB',
            },
        ),
    ]