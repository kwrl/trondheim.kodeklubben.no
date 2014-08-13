from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from .permissions import IsStaffOrTargetUser
from .serializers import UserSerializer

class UserView(viewsets.ViewSet):
    queryset = User.objects.all() 

    def list(self, request):
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),
    @action(["GET","POST"])
    def login(request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return Response({'status':'Logged in'})
            return Response({'status':'User not active'})
        return Response({'status':'Incorrect credentials'})

    @action(["GET","POST"])
    def logout(request):
        logout(request)
        return Response({'status':'User logged out'})
