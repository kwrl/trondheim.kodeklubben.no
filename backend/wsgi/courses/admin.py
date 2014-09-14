from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from .models import Course, Registration, Ranking, ScoreProfile

def get_course_lists(modeladmin, request, queryset):
    for course in queryset:
        granted = Registration.objects.filter(course=course, granted=True)
        course.granted_masters  = granted.filter(code_master=True) 
        course.granted_kids     = granted.filter(code_master=False)
    return render(request, 'courses/course_list.html', {'courses':queryset})

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

get_course_lists.short_description = "Get course lists"

export_as_json.short_description = "Export registrations as JSON"
grant_registrations.short_description = "Grant registrations"
remove_grants.short_description = "Ungrant registrations"

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('course','user','granted', 'code_master')
    list_filter = ('granted','code_master','course','user')
    actions = [export_as_json, grant_registrations, remove_grants]

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','desc')
    actions = [get_course_lists, export_as_json]


admin.site.register(Course,CourseAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Ranking)
admin.site.register(ScoreProfile)
