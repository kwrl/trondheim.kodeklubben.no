from rest_framework import status, viewsets, permissions
from rest_framework.decorators import api_view, action, link
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .serializers import CourseHeaderSerializer, CourseFullSerializer 
from .models import Course, Registration

def list_courses(request):
    queryset = Course.objects.all()

    for course in queryset:
        course.taken = Registration.objects.filter(course=course).count()

    if(request.user.is_authenticated()):
        for course in queryset:
            course.signed_up = course.registrations.filter(user=request.user).count()
    

    context = {}

    context['courses'] = queryset

    return render(request, 'courses/courses.html',context)

@login_required
def register(request):
    course_id = request.POST['course_id']
    user_id = request.user.id
    sign_up = request.POST['sign_up']==u'1'

    course = Course.objects.get(pk=course_id)
    #import ipdb
    #ipdb.set_trace()
    if not course:
        return

    if sign_up and not Registration.objects.filter(user=request.user, course=course).exists():
        Registration(user=request.user, course=course, granted=False).save()
    else:
        Registration.objects.filter(user=request.user, course=course).delete()

class CourseView(viewsets.ViewSet):
    queryset = Course.objects.filter(registration_end__gt=timezone.now()).filter(registration_start__lt=timezone.now())

    def list(self, request):
        serializer = CourseHeaderSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        course = get_object_or_404(self.queryset, pk=pk)
        serializer = CourseFullSerializer(course)
        return Response(serializer.data)

    @action(methods=['POST'])
    def register(self, request, pk=None):
        course  = get_object_or_404(self.get_open_courses(), pk=pk)
        user    = request.user

        if Registration.objects.filter(course=course, user=user).exists():
            return Response({'status': 'already registered'})

        Registration(course=course, user=user, granted=False).save()
        return Response({'status': 'registration successful'})

    @action(methods=['POST'])
    def unregister(self,request, pk=None):
        course  = get_object_or_404(self.queryset, pk=pk)
        user    = request.user

        if Registration.objects.filter(course=course, user=user).exists():
            Registration.objects.filter(course=course, user=user).delete()
            return Response({'status':'removed registration successfully'})

        return Response({'status':'no such registration'}) 

    #@action(methods=['GET'])
    #def get_granted(self, requert, pk=None):
    #    registrations = Registration.objects.filter(user=request.user)



class FullCourseView(viewsets.ViewSet):
    queryset = Course.objects.all()

    def list(self, request):
        serializer = CourseHeaderSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        course = get_object_or_404(self.queryset, pk=pk)
        serializer = CourseFullSerializer(course)
        return Response(serializer.data)








