from rest_framework import status, viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

from .serializers import CourseHeaderSerializer, CourseFullSerializer 
from .models import Course, Registration

class CourseView(viewsets.ViewSet):
    queryset = Course.objects.filter(registration_end__gt=datetime.now())

    def list(self, request):
        serializer = CourseHeaderSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        course = get_object_or_404(self.queryset, pk=pk)
        serializer = CourseFullSerializer(course)
        return Response(serializer.data)

