# Generated by Django 3.1 on 2021-04-22 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210422_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecategory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='homecategory', to='home.category', verbose_name='选择分类'),
        ),
    ]
