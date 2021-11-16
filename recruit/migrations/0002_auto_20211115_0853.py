# Generated by Django 3.2.9 on 2021-11-15 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0001_initial'),
        ('recruit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='document',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document', to='recruit.document'),
        ),
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='score', to='score.score'),
        ),
    ]