from rest_framework import status, viewsets, permissions
from rest_framework.decorators import api_view, action, link
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .serializers import CourseHeaderSerializer, CourseFullSerializer 
from .models import Course, Registration

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


class FullCourseView(viewsets.ViewSet):
    queryset = Course.objects.all()

    def list(self, request):
        serializer = CourseHeaderSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        course = get_object_or_404(self.queryset, pk=pk)
        serializer = CourseFullSerializer(course)
        return Response(serializer.data)

   






