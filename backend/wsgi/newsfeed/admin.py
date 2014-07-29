from django.contrib import admin
from models import NewsItem
class NewsItemAdmin(admin.ModelAdmin):
    fieldset = (
        (None, {
            'fields':('title', 'intro','body'),
        })
    )

    list_display = ('title','time_stamp')
    search_fields = ('title','intro','body')
    
    ordering = ('time_stamp',)

admin.site.register(NewsItem, NewsItemAdmin)
