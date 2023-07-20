from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class DeliciousWayAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    fields = (
    'title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
        else:
            return "Нет фото"

    get_html_photo.short_description = "фото"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'content')
    ordering = ('-created_at',)


admin.site.register(DeliciousWay, DeliciousWayAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Feedback)

admin.site.site_title = 'Админ-панель сайта "Вкусный путь"'
admin.site.site_header = 'Админ-панель сайта "Вкусный путь"'

