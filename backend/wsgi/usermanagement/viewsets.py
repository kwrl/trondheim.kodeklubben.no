from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.queryset.filter(pk=self.request.user.pk)
