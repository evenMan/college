from django.contrib import admin
from home.models import Article
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'preview')

    def preview(self, obj):
        return  mark_safe('<img src="http://127.0.0.1:8000/media/%s" height="49" width="49" />' % obj.image)
    preview.allow_tags = True
    preview.short_description = "图片"

    # 字段,控制分页,每页返回的数量
    list_per_page = 20