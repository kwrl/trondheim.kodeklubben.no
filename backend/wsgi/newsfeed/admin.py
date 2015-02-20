from django.contrib import admin
from .models import NewsItem
from .forms import NewsItemForm

class NewsItemAdmin(admin.ModelAdmin):
    fieldset = (
        (None, {
            'fields':('title', 'intro','body'),
        })
    )
    list_display = ('title','time_stamp')
    search_fields = ('title','intro','body')
    ordering = ('time_stamp',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
            return db_field.formfield(**kwargs)
        return super(NewsItemAdmin, self).formfield_for_foreignkey(db_field,
                                                                   request,
                                                                   **kwargs)
    class Media:
        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        '/static/grappelli/tinymce_setup/tinymce_setup.js']

admin.site.register(NewsItem, NewsItemAdmin)
