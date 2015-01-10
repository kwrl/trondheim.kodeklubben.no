from django import forms
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Course, Registration, Ranking, ScoreProfile, Task, TaskSubmission

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

class CourseAdminForm(forms.ModelForm):
    tasks = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=('Tasks'),
            is_stacked=False
        )
    )
    class Meta:
        model = Course

    def __init__(self, *args, **kwargs):
        super(CourseAdminForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['tasks'].initial = self.instance.tasks.all()

    def save(self, commit=True):
        course = super(CourseAdminForm, self).save(commit=False)

        if commit:
            course.save()
        if course.pk:
            course.tasks= self.cleaned_data['tasks']
            self.save_m2m()
        return course

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('course','user','granted', 'code_master')
    list_filter = ('granted','code_master','course','user')
    actions = [export_as_json, grant_registrations, remove_grants]

class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = ('name','desc')
    actions = [get_course_lists, export_as_json]

admin.site.register(Task)
admin.site.register(Course,CourseAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Ranking)
admin.site.register(ScoreProfile)
admin.site.register(TaskSubmission)
