# Generated by Django 3.2.9 on 2021-11-16 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0005_document_interview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='cert_web',
        ),
    ]
