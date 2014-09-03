from django.http import HttpResponse
#from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
#from rest_framework import viewsets
#from rest_framework.permissions import AllowAny
#from rest_framework.decorators import action, api_view
#from rest_framework.response import Response
#from rest_framework.renderers import JSONPRenderer, JSONRenderer
#from rest_framework.serializers import LoginSerializer
#from rest_framework.views import APIView

from datetime import datetime
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .forms import UserCreateForm, UserEditForm
from django.conf import settings
from django.contrib import auth
from django.views.generic import View
from class_based_auth_views.views import LogoutView

from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

#from .permissions import IsStaffOrTargetUser
#from .serializers import UserSerializer 

class EditUserView(View):
    form_class = UserEditForm
    template_name = 'user_name_screen.html'
    
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {'form':form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
        return redirect(reverse('home'))


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return redirect(reverse('home'))
    
    return redirect(reverse('log_in'))

class UserCreateView(CreateView):
    template_name = "register_screen.html"
    model = User 
    form_class = UserCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_date = datetime.now()
        form.save()
        return super(UserCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('log_in') 

class LogoutView(LogoutView):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated():
            if(settings.LOGOUT_REDIRECT_URL):
                return redirect(settings.LOGOUT_REDIRECT_URL)
            else:
                return redirect(self.get_redirect_url())
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            auth.logout(self.request)
        if(settings.LOGOUT_REDIRECT_URL):
            return redirect(settings.LOGOUT_REDIRECT_URL)
        
        return redirect(self.get_redirect_url())

"""
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

"""
