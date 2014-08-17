from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONPRenderer, JSONRenderer
from rest_framework.serializers import LoginSerializer
from rest_framework.views import APIView

from .permissions import IsStaffOrTargetUser
from .serializers import UserSerializer

@method_decorator(ensure_csrf_cookie)
class LoginView(APIView):
    renderer_classes = (JSONPRenderer, JSONRenderer)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.DATA)
        if serializer.is_valid():
            userAuth = authenticate(username=serializer.data['username'], password=serializer.data['password'])
            if userAuth:
                if userAuth.is_active:
                    login(request, userAuth)
                    loggedInUser = AuthUserProfile.objects.get(pk=1)
                    serializer = UserProfileSerializer(loggedInUser)
                    user = [serializer.data, {'isLogged': True}]
            else:
                user = {'isLogged': False}
            return Response(user, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
