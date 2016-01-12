from django.conf.urls import patterns, url
from rest_framework import routers

from .viewsets import OpenCourseViewSet

from .views import \
    CourseRegistrationView, \
    ProfileView, \
    CourseListView, \
    TaskSubmissionView, \
    CourseListJSON

urlpatterns = patterns('',
                       url(r'^$',
                           CourseListView.as_view(),
                           name="course_list"),
                       url(r'^open_courses_json/',
                           CourseListJSON.as_view(),
                           name="open_courses_json"),
                       url(r'^register/(?P<course_id>\d+)/$',
                           CourseRegistrationView.as_view(),
                           name="course_register"),
                       url(r'^profile/',
                           ProfileView.as_view(),
                           name="view_profile"),
                       url(r'^task/(?P<task_id>\d+)',
                           TaskSubmissionView.as_view(),
                           name="submit_to_task"))
