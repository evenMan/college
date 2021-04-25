import json

from django.core import serializers
from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from home.models import HomeCategory,Location, Category
# Create your views here.

from django.middleware.csrf import get_token


def getToken(request):
    token = get_token(request)
    return HttpResponse(json.dumps({'token': token}), content_type="application/json,charset=utf-8")


# 首页分类接口
def ClassifyList(request):
    # 和前端约定的返回格式
    result = {"message": 'success', "code": '200', "data": []}

    try:
        # 获取列表数据
        category = Category.objects.all()
    except Exception as result:
        print("捕获到了异常，信息是:%s" % result)

    # 序列化数据列表
    json_string = serializers.serialize('json', category)
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
    result['totalCount'] = category.count()
    # 转换为 JSON 字符串并返回
    return JsonResponse(result)



# 首页列表接口
def HomeList(request):
    # 和前端约定的返回格式
    result = {"message": 'success', "code": '200', "data": []}

    try:
        # 获取列表数据
        article = HomeCategory.objects.all()
    except Exception as result:
        print("捕获到了异常，信息是:%s" % result)

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
        if model.video:
            model.video = request.scheme + '://' + request.META['HTTP_HOST'] + '/media/' + model.video.__str__()
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


# 商品详情
def HomeDetails(request):
    # 接收数据
    id = request.POST.get('id')
    print('id')
    print(id)

    # 判断文章是否存在
    try:
        details = HomeCategory.objects.filter(pk=id)

        result = {"message": 'success', "code": '200', "data": []}

        # 拼接图片路径
        for model in details:
            model.homeImage = request.scheme + '://' + request.META['HTTP_HOST'] + '/media/' + model.homeImage.__str__()
            if model.video:
                model.video = request.scheme + '://' + request.META['HTTP_HOST'] + '/media/' + model.video.__str__()
            if model.bannerOne:
                model.bannerOne = request.scheme + '://' + request.META['HTTP_HOST'] + '/media/' + model.bannerOne.__str__()
            if model.bannerSecond:
                model.bannerSecond = request.scheme + '://' + request.META['HTTP_HOST'] + '/media/' + model.bannerSecond.__str__()
        json_string = serializers.serialize('json', details)
        data = json.loads(json_string)
        arr = []
        arr2 = []
        for item in data:
            item['fields']['id'] = item['pk']
            arr.append(item['fields'])

        # 赋值给data
        result['data'] = arr
    except HomeCategory.DoesNotExist:
        result = {"message": 'success', "code": '404', "data": []}
        return JsonResponse(result)
    # 转换为 JSON 字符串并返回
    return JsonResponse(result)









