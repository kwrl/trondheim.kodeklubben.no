from django.http import HttpResponse
from django.core import serializers as ser
from django.contrib.auth.decorators import login_required
from datetime import datetime
from models import Course, Registration

#Gets all course headers that have yet to close registration
def get_course_headers(request):
    courses = Course.objects.filter(registration_end__gt=datetime..now())
    data = ser.serialize('json', courses, fields='id','name')
    return HttpResponse(data)
    
def get_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    data = ser.serialize('json', [course])
    return HttpResponse(data)

@login_required
def register_course(request, course_id):
    course  = Course.objects.get(pk=course_id)
    pass

@login_required
def deregister_course(request, course_id):
    course  = Course.objects.get(pk=course_id)
    pass
