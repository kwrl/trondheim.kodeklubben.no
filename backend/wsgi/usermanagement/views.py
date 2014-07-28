from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .permissions import IsStaffOrTargetUser
from .serializers import UserSerializer

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User

    def get_permissions(self):
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),
