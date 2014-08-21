from django.contrib import admin

from .models import Course, Registration

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','desc')

admin.site.register(Course,CourseAdmin)
admin.site.register(Registration)
