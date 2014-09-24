from django.conf.urls import patterns, include, url

from .views import list_courses, register, view_profile, TaskSubmissionView

urlpatterns = patterns('',
        url(r'^list/$', list_courses),
        url(r'^register/',register, name="course_register"),
        url(r'^profile/', view_profile, name="view_profile"),
        url(r'^task/(?P<task_id>\d+)', TaskSubmissionView.as_view(), name="submit_to_task"),
)
