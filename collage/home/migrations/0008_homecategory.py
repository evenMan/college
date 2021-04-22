# Generated by Django 3.1 on 2021-04-22 06:52

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210422_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='主标题')),
                ('homeImage', models.ImageField(blank=True, upload_to='home/%Y%m%d%H%M%S', verbose_name='主图片')),
                ('home_desc', models.TextField(blank=True, max_length=500, verbose_name='介绍说明')),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('endTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='结束时间')),
                ('allNum', models.IntegerField(default=0, verbose_name='总库存数')),
                ('desc_pack', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='商品详情')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.category')),
            ],
            options={
                'verbose_name': '首页列表',
                'verbose_name_plural': '首页列表',
                'db_table': 'tb_homeList',
            },
        ),
    ]
