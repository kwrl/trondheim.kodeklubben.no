from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from .forms import TaskAdminForm, CourseAdminForm
from .models import \
    Course, Registration, Ranking, ScoreProfile, Task, TaskSubmission


def get_course_lists(modeladmin, request, queryset):
    for course in queryset:
        granted = Registration.objects.filter(course=course, granted=True)
        course.granted_masters = granted.filter(code_master=True)
        course.granted_kids = granted.filter(code_master=False)
        return render(request,
                      'courses/course_list.html',
                      {'courses': queryset})


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
    list_display = ('course', 'user', 'granted', 'role')
    list_filter = ('granted', 'course', 'user', 'role')
    actions = [export_as_json, grant_registrations, remove_grants]


class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = ('name', 'desc')
    actions = [get_course_lists, export_as_json]


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',)

    class Media:
        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        '/static/grappelli/tinymce_setup/tinymce_setup.js']

class TaskSubmissionAdmin(admin.ModelAdmin):
    list_display = ('task',
                    'submitted_by',
                    'valid',
                    'submitted_at',
                    'content_file_link')

    list_filter = ('task',
                   'submitted_by',
                   'valid',
                   'submitted_at')


class RankingAdmin(admin.ModelAdmin):
    list_display = ('name', 'required_score')
    list_filter = ('name', 'required_score')

admin.site.register(Task, TaskAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Ranking, RankingAdmin)
admin.site.register(ScoreProfile)
admin.site.register(TaskSubmission, TaskSubmissionAdmin)
