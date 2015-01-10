from django.conf.urls import patterns, url

from .views import \
    CourseRegistrationView, \
    ProfileView, \
    CourseListView, \
    TaskSubmissionView

urlpatterns = patterns('',
                       url(r'^$',
                           CourseListView.as_view(),
                           name="course_list"),
                       url(r'^register/',
                           CourseRegistrationView.as_view(),
                           name="course_register"),
                       url(r'^profile/',
                           ProfileView.as_view(),
                           name="view_profile"),
                       url(r'^task/(?P<task_id>\d+)',
                           TaskSubmissionView.as_view(),
                           name="submit_to_task"))
