from django.contrib import admin
from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.db import models
from .forms import TaskAdminForm, CourseAdminForm
from .models import \
    Course, Registration, Ranking, ScoreProfile, Task, TaskSubmission

from django.utils.translation import gettext_lazy as _
from django.utils import timezone


def export_csv(modeladmin, request, queryset):
    return StreamingHttpResponse(request, str(models.get_models(include_auto_created=True)))

def get_course_lists(modeladmin, request, queryset):
    for course in queryset:
        granted = Registration.objects.filter(course=course, granted=True)
        course.granted_masters = granted.filter(role=Registration.CODE_MASTER)
        course.granted_reserves = granted.filter(role=Registration.RESERVE)
        course.granted_kids = granted.filter(role=Registration.KID)
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
export_csv.short_description = "Export lol"

class OpenRegistrationFilter(admin.SimpleListFilter):
    title = _('Pending/open/closed')
    parameter_name = 'state'

    def lookups(self, request, model_admin):
        return (
            ('open', _('Registrations for open courses ')),
            ('pending', _('Registrations for pending courses')),
            ('closed', _('Registrations for closed courses'))
        )

    def queryset(self, request, queryset):
        courses = None
        if self.value() == 'open':
            courses = Course.objects.filter(registration_start__lt=timezone.now(),
                                      registration_end__gt=timezone.now())
        if self.value() == 'pending':
            courses = Course.objects.filter(registration_start__gt=timezone.now())

        if self.value() == 'closed':
            courses = Course.objects.filter(registration_end__lt=timezone.now())

        if courses == None:
            return queryset

        return queryset.filter(course__in=courses)


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'granted', 'role')
    list_filter = (OpenRegistrationFilter, 'granted', 'course', 'user', 'role')
    actions = [export_as_json, grant_registrations, remove_grants, export_csv]

class OpenCourseFilter(admin.SimpleListFilter):
    title = _('Pending/open/closed')
    parameter_name = 'state'
    def lookups(self, request, model_admin):
        return (
            ('open', _('Courses currently open for registration')),
            ('pending', _('Courses that have not been opened')),
            ('closed', _('Courses that have been closed'))
        )

    def queryset(self, request, queryset):
        if self.value() == 'open':
            return queryset.filter(registration_start__lt=timezone.now(),
                                      registration_end__gt=timezone.now())
        if self.value() == 'pending':
            return queryset.filter(registration_start__gt=timezone.now())

        if self.value() == 'closed':
            return queryset.filter(registration_end__lt=timezone.now())

        return queryset


class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = ('name', 'desc')
    list_filter = (OpenCourseFilter, )
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
