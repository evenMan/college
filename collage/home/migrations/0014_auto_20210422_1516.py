# Generated by Django 3.1 on 2021-04-22 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20210422_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecategory',
            name='allNum',
            field=models.IntegerField(blank=True, default=0, verbose_name='总库存数'),
        ),
    ]
