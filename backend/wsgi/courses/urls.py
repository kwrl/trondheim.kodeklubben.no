from django.conf.urls import patterns, include, url

from .views import \
    register, \
    view_profile, \
    CourseListView, \
    TaskSubmissionView

urlpatterns = patterns('',
        url(r'^$', CourseListView.as_view(), name="course_list"),
        url(r'^register/',register, name="course_register"),
        url(r'^profile/', view_profile, name="view_profile"),
        url(r'^task/(?P<task_id>\d+)', TaskSubmissionView.as_view(), name="submit_to_task"),
)
