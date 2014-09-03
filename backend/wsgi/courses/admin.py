from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from .models import Course, Registration

def get_course_lists(modeladmin, request, queryset):
    for course in queryset:
        course.granted_regs = Registration.objects.filter(course=course, granted=True)
    return render(request, 'courses/course_list.html', {'courses':queryset})

get_course_lists.short_description = "Get course lists"

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','desc')
    actions = [get_course_lists]

def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response

def grant_registrations(modeladmin, request, queryset):
    queryset.update(granted=True)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove_grants(modeladmin, request, queryset):
    queryset.update(granted=False)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

export_as_json.short_description = "Export registrations as JSON"
grant_registrations.short_description = "Grant registrations"
remove_grants.short_description = "Ungrant registrations"

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('course','user','granted', 'code_master')
    list_filter = ('granted','code_master','course','user')
    actions = [export_as_json, grant_registrations, remove_grants]


admin.site.register(Course,CourseAdmin)
admin.site.register(Registration, RegistrationAdmin)
