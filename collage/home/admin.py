from django.contrib import admin
from django.utils.safestring import mark_safe
from home.models import Article, Category, Location, HomeCategory, Users

# Register your models here.

# 用户信息
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    def preview(self, obj):
        return  mark_safe('<img src="obj.avatarUrl" height="49" width="49" />')
    preview.allow_tags = True
    preview.short_description = "图片"
    list_display = ['nickName', 'gender', 'country', 'province', 'city', 'phone', 'expert']
    search_fields = ('nickName',)


#位置
admin.site.register(Location)

# 分类
admin.site.register(Category)

# 首页列表
@admin.register(HomeCategory)
class HomeCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'createTime', 'endTime']


# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'created', 'preview')
#
#     def preview(self, obj):
#         return  mark_safe('<img src="http://127.0.0.1:8000/media/%s" height="49" width="49" />' % obj.image)
#     preview.allow_tags = True
#     preview.short_description = "图片"
#
#     # 字段,控制分页,每页返回的数量
#     list_per_page = 20

















