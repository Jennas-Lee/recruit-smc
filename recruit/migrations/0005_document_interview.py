# Generated by Django 3.2.9 on 2021-11-16 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0004_rename__class_student_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='interview',
            field=models.JSONField(default=''),
            preserve_default=False,
        ),
    ]
