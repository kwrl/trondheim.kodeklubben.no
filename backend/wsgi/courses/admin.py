from django.contrib import admin

from .models import Course, Registration

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','desc')

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('course','user','granted', 'code_master')
    list_filter = ('granted','code_master','course','user')

admin.site.register(Course,CourseAdmin)
admin.site.register(Registration, RegistrationAdmin)
