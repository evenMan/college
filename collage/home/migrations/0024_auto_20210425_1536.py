# Generated by Django 3.1 on 2021-04-25 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20210425_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecategory',
            name='bannerOne',
            field=models.ImageField(blank=True, default='', null=True, upload_to='home/%Y%m%d%H%M%S61740', verbose_name='轮播图1(非必传)'),
        ),
        migrations.AlterField(
            model_name='homecategory',
            name='bannerSecond',
            field=models.ImageField(blank=True, default='', null=True, upload_to='home/%Y%m%d%H%M%S61740', verbose_name='轮播图2(非必传)'),
        ),
        migrations.AlterField(
            model_name='homecategory',
            name='homeImage',
            field=models.ImageField(upload_to='home/%Y%m%d%H%M%S61740', verbose_name='主图片'),
        ),
        migrations.AlterField(
            model_name='homecategory',
            name='video',
            field=models.FileField(blank=True, default='', null=True, upload_to='home/videos/%Y%m%d%H%M%S61740', verbose_name='视频上传(非必传)'),
        ),
    ]