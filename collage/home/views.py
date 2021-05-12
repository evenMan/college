import json

import requests
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage
from django.db import DatabaseError
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse, request, HttpResponseBadRequest
from django.shortcuts import render
from home.models import HomeCategory,Location, Category, Users
import base64
from Crypto.Cipher import AES

# Create your views here.

from django.middleware.csrf import get_token

from utils.WXBizDataCrypt import WXBizDataCrypt


def getToken(request):
    token = get_token(request)
    return HttpResponse(json.dumps({'token': token}), content_type="application/json,charset=utf-8")


# 获取微信小程序opneid
def get_code(request):
    JSCODE = request.POST.get("code")
    encryptedData = request.POST.get("encryptedData")
    iv = request.POST.get("iv")
    APPID = "wx19d2ad3ecd9ee6f8"
    SECRET = "79e5ea7a3420a877831b8b8b949da446"
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type=authorization_code'.format(
        appid=APPID, secret=SECRET, code=JSCODE)
    res = requests.get(url)
    return JsonResponse(res.json())

def decrypt(request):
    openid = request.POST.get("openid")
    session_key = request.POST.get("sessionKey")
    encryptedData1 = request.POST.get("encryptedData")
    iv1 = request.POST.get("iv")

    sessionKey = base64.b64decode(session_key)
    encryptedData = base64.b64decode(encryptedData1)
    iv = base64.b64decode(iv1)
    cipher = AES.new(sessionKey, AES.MODE_CBC, iv)
    s = cipher.decrypt(encryptedData)
    unpad = s[:-ord(s[len(s) - 1:])]
    decrypted = json.loads(unpad)
    print(decrypted['phoneNumber'])
    user = Users.objects.get(openid=openid)
    print(user)
    user.phone = decrypted['phoneNumber']
    user.save()

    result = {"message": 'success', "code": '200', "data": '登录成功!'}
    return JsonResponse(result)


# 用户注册信息
def RegisterUsers(request):
    # 接收参数
    openid = request.POST.get('openid')
    session_key = request.POST.get('session_key')
    avatarUrl = request.POST.get('avatarUrl')
    nickName = request.POST.get('nickName')
    gender = request.POST.get('gender')
    country = request.POST.get('country')
    province = request.POST.get('province')
    city = request.POST.get('city')

    # 判断参数是否齐全
    if not all([openid, session_key, avatarUrl, nickName]):
        return HttpResponseBadRequest('缺少必传参数')

    try:
        result = {"message": 'success', "code": '200', "data": []}
        user = Users.objects.filter(openid=openid)
        json_string = serializers.serialize('json', user)
        data = json.loads(json_string)
        arr = []
        arr2 = []
        for item in data:
            item['fields']['id'] = item['pk']
            arr.append(item['fields'])
        # 赋值给data
        result['data'] = arr
        return JsonResponse(result)
    except Users.DoesNotExist:
        # 保存注册数据
        try:
            user = Users.objects.create(openid=openid, session_key=session_key, avatarUrl=avatarUrl, nickName=nickName,
                                        gender=gender, country=country, province=province, city=city)
            result = {"message": 'success', "code": '200', "data": '注册成功!'}
            return JsonResponse(result)
        except DatabaseError:
            return JsonResponse('注册失败')


#查询用户信息
def GetUserInfo(request):
    openid = request.POST.get('openid')

    # 和前端约定的返回格式
    result = {"message": 'success', "code": '200', "data": []}
    try:
        user = Users.objects.filter(openid=openid)
        # 序列化数据列表
        json_string = serializers.serialize('json', user)
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
        return JsonResponse(result)
    except DatabaseError:
        return JsonResponse('获取失败')



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
        if model.poster:
            model.poster = request.scheme + '://' + request.META['HTTP_HOST'] + '/media/' + model.poster.__str__()
    # 序列化数据列表
    json_string = serializers.serialize('json', page_article, fields=('title', 'homeImage', 'location', 'category', 'allNum', 'home_desc', 'createTime', 'endTime', 'originPrices', 'prices'))
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

# 分类列表
# 首页列表接口
def HomeClassifyList(request):
    # 和前端约定的返回格式
    result = {"message": 'success', "code": '200', "data": []}
    category_id = request.GET.get('category_id')
    try:
        # 获取列表数据
        article = HomeCategory.objects.filter(category_id=category_id)
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
        if model.poster:
            model.poster = request.scheme + '://' + request.META['HTTP_HOST'] + '/media/' + model.poster.__str__()
    # 序列化数据列表
    json_string = serializers.serialize('json', page_article, fields=('title', 'homeImage', 'location', 'category', 'allNum', 'home_desc', 'createTime', 'endTime', 'originPrices', 'prices'))
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
            if model.poster:
                model.poster = request.scheme + '://' + request.META['HTTP_HOST'] + '/media/' + model.poster.__str__()
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









