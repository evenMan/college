# Generated by Django 3.1 on 2021-04-28 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20210427_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='expert',
            field=models.BooleanField(default=False, verbose_name='是否开通达人'),
        ),
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=11, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='homecategory',
            name='bannerOne',
            field=models.ImageField(blank=True, default='', max_length=300, null=True, upload_to='home/%Y%m%d%H%M%S52124', verbose_name='轮播图1(非必传)'),
        ),
        migrations.AlterField(
            model_name='homecategory',
            name='bannerSecond',
            field=models.ImageField(blank=True, default='', max_length=300, null=True, upload_to='home/%Y%m%d%H%M%S52124', verbose_name='轮播图2(非必传)'),
        ),
        migrations.AlterField(
            model_name='homecategory',
            name='homeImage',
            field=models.ImageField(max_length=300, upload_to='home/%Y%m%d%H%M%S52124', verbose_name='主图片'),
        ),
        migrations.AlterField(
            model_name='homecategory',
            name='video',
            field=models.FileField(blank=True, default='', max_length=300, null=True, upload_to='home/videos/%Y%m%d%H%M%S52124', verbose_name='视频上传(非必传)'),
        ),
        migrations.AlterField(
            model_name='users',
            name='avatarUrl',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='头像'),
        ),
    ]
