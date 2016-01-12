from rest_framework import viewsets

from .serializers import CourseSerializer
from .models import Course, Registration

class OpenCourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.open_registration()
    serializer_class = CourseSerializer
