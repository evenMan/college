# Generated by Django 3.1 on 2021-04-22 08:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20210422_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
    ]
