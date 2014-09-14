from django.conf.urls import patterns, include, url

from .views import list_courses, register, view_profile

urlpatterns = patterns('',
        url(r'^list/$', list_courses),
        url(r'^register/',register, name="course_register"),
        url(r'^profile/', view_profile, name="view_profile"),
)
