import random

from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# 用户信息
class Users(models.Model):
    openid = models.CharField(max_length=100, null=False, blank=False)
    session_key = models.CharField(max_length=100, null=False, blank=False)
    expert = models.BooleanField(default=False, verbose_name='是否开通达人')
    avatarUrl = models.CharField(max_length=300, default='', blank=True, verbose_name='头像')
    nickName = models.CharField(max_length=100, default='', blank=True, verbose_name='昵称')
    gender = models.CharField(max_length=100, default='', blank=True, verbose_name='性别')
    country = models.CharField(max_length=100, default='', blank=True, verbose_name='国家')
    province = models.CharField(max_length=100, default='', blank=True, verbose_name='省份')
    city = models.CharField(max_length=100, default='', blank=True, verbose_name='城市')
    phone = models.CharField(max_length=11, default='', blank=True, verbose_name='手机号')

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

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
    random_string = str(random.randint(10000, 99999))
    # 首页主图
    homeImage = models.ImageField(max_length=300, upload_to='home/%Y%m%d%H%M%S'+random_string, verbose_name='主图片')
    # 轮播图1
    bannerOne = models.ImageField(max_length=300, upload_to='home/%Y%m%d%H%M%S'+random_string, default='', blank=True, null=True, verbose_name='轮播图1(非必传)')
    # 轮播图2
    bannerSecond = models.ImageField(max_length=300, upload_to='home/%Y%m%d%H%M%S'+random_string, default='', blank=True, null=True, verbose_name='轮播图2(非必传)')
    # 视频上传
    video = models.FileField(max_length=300, upload_to='home/videos/%Y%m%d%H%M%S'+random_string,default='', blank=True, null=True, verbose_name='视频上传(非必传)')
    # 上传海报
    poster = models.ImageField(max_length=300, upload_to='home/%Y%m%d%H%M%S'+random_string, default='', blank=True, null=True, verbose_name='上传海报(必传)')
    # 所在城市
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE, related_name='homecategory',verbose_name='所在城市')
    # 分类
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, related_name='homecategory', verbose_name='选择分类')
    # 套餐标题
    setMeal = models.CharField(max_length=100, default='', blank=False, null=False, verbose_name='套餐标题')
    # 总库存数量
    allNum = models.IntegerField(default=0, blank=True, verbose_name='总库存数')
    # 原价
    originPrices = models.FloatField(default=0.00, blank=True, verbose_name='原价格')
    # 现价
    prices = models.FloatField(default=0.00, blank=True, verbose_name='现价格')
    # 创建时间
    createTime = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    # 结束时间
    endTime = models.DateTimeField(default=timezone.now, verbose_name='结束时间')
    # 地址
    address = models.CharField(max_length=200, default='', blank=False, null=False, verbose_name='地址详情')
    # 电话
    mobile = models.CharField(max_length=100, default='', blank=False, null=False, verbose_name='商家电话')
    # 老板有话说
    bossSay = models.CharField(max_length=200,default='', blank=False, null=False, verbose_name='老板有话说')
    #精度
    longitude = models.FloatField(default=0.00, blank=True, verbose_name='精度')
    # 纬度
    latitude = models.FloatField(default=0.00, blank=True, verbose_name='纬度')
    # 美食介绍
    home_desc = models.TextField(max_length=500, blank=True, null=True, verbose_name='介绍说明')
    # 商品详情
    desc_pack = RichTextUploadingField(default='',blank=True, null=True, verbose_name='商品详情')


    class Meta:
        db_table = 'tb_homeList'
        verbose_name = '首页列表'
        verbose_name_plural = verbose_name











