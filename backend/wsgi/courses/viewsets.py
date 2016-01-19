from rest_framework import viewsets
from rest_framework import mixins

from .serializers import CourseSerializer, RegistrationSerializer
from .models import Course, Registration

class OpenCourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.open_registration()
    serializer_class = CourseSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    

       
