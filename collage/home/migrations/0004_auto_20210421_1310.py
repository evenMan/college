# Generated by Django 3.1 on 2021-04-21 05:10

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210421_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='details',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='文章详情'),
        ),
    ]
