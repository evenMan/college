# Generated by Django 3.1 on 2021-04-22 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210422_1355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '家装知识', 'verbose_name_plural': '家装知识'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '分类', 'verbose_name_plural': '分类'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': '城市位置', 'verbose_name_plural': '城市位置'},
        ),
    ]
