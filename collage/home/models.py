from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# 文章功能
class Article(models.Model):

    # 文章标题
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='文章标题')
    # 作者
    author = models.CharField(max_length=10, default='', blank=True, verbose_name='作者')
    # 文章图片
    image = models.ImageField(upload_to='home/%Y%m%d%H%M%S', blank=True, verbose_name='上传图片')
    # 创建时间
    created = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    # 文章详情
    details = RichTextUploadingField(default='', verbose_name='文章详情')

    class Meta:
        db_table = 'tb_article'
        verbose_name = '家装知识'
        verbose_name_plural = verbose_name


#  位置
class Location(models.Model):
    # 标题
    location = models.CharField(max_length=100, blank=True, verbose_name='所在城市')
    # 创建时间
    created = models.DateTimeField(default=timezone.now, verbose_name='创建时间')

    def __str__(self):
        return self.location

    class Meta:
        db_table = 'tb_location'
        verbose_name = '城市位置'
        verbose_name_plural = verbose_name

#  分类
class Category(models.Model):
    # 标题
    title = models.CharField(max_length=100, blank=True, verbose_name='分类标题')
    # 创建时间
    created = models.DateTimeField(default=timezone.now, verbose_name='创建时间')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tb_category'
        verbose_name = '首页分类'
        verbose_name_plural = verbose_name


# 美食
class HomeCategory(models.Model):
    # 美食标题
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='主标题')
    # 首页主图
    homeImage = models.ImageField(upload_to='home/%Y%m%d%H%M%S', verbose_name='主图片')
    # 所在城市
    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.CASCADE, related_name='homecategory',verbose_name='所在城市')
    # 分类
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name='homecategory', verbose_name='选择分类')
    # 总库存数量
    allNum = models.IntegerField(default=0, blank=True, verbose_name='总库存数')
    # 美食介绍
    home_desc = models.TextField(max_length=500, blank=True, verbose_name='介绍说明')
    # 创建时间
    createTime = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    # 结束时间
    endTime = models.DateTimeField(default=timezone.now, verbose_name='结束时间')
    # 商品详情
    desc_pack = RichTextUploadingField(default='', verbose_name='商品详情')

    class Meta:
        db_table = 'tb_homeList'
        verbose_name = '首页列表'
        verbose_name_plural = verbose_name














