import json

from django.core import serializers
from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render
from home.models import HomeCategory
# Create your views here.

def HomeList(request):
    # 和前端约定的返回格式
    result = {"message": 'success', "code": '200', "data": []}

    # 获取列表数据
    article = HomeCategory.objects.all()

    # 第几页
    page_num = request.GET.get('pageNum')
    # 每页多少条
    page_size = request.GET.get('pageSize')

    # 创建分页器：每页N条记录
    paginator = Paginator(article, page_size)
    # 获取每页数据

    try:
        page_article = paginator.page(page_num)
    except EmptyPage:
        return JsonResponse(result)

    # 拼接图片路径
    for model in page_article:
        model.homeImage = request.scheme + '://' + request.META['HTTP_HOST'] + '/media/' + model.homeImage.__str__()
        # if model.video:
        #     model.video = request.scheme + '://' + request.META['HTTP_HOST'] + '/media/' + model.video.__str__()
    # 序列化数据列表
    json_string = serializers.serialize('json', page_article, fields=('title', 'homeImage', 'location', 'category', 'allNum', 'home_desc', 'createTime', 'endTime'))
    # 字符串转json
    data = json.loads(json_string)
    # 取出fields内容，去除model、pk，fields
    arr = []
    arr2 = []
    for item in data:
        item['fields']['id'] = item['pk']
        arr.append(item['fields'])

    # 赋值给data
    result['data'] = arr
    # 总数
    result['totalCount'] = article.count()
    # 转换为 JSON 字符串并返回
    return JsonResponse(result)