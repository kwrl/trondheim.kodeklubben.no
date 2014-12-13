from django.contrib import admin
from .models import Sponsor


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name', 'url')
    ordering = ('name',)

admin.site.register(Sponsor, SponsorAdmin)
