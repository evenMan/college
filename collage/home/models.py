from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Article(models.Model):

    # 文章标题
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='文章标题')
    # 作者
    author = models.CharField(max_length=10, default='', blank=True, verbose_name='作者')
    # 文章图片
    image = models.ImageField(upload_to='media/home/%Y%m%d%H%M%S', blank=True, verbose_name='上传图片')
    # 创建时间
    created = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    # 文章详情
    details = RichTextUploadingField(default='', verbose_name='')

    class Meta:
        db_table = 'tb_article'
        verbose_name = '家装知识管理'
        verbose_name_plural = verbose_name