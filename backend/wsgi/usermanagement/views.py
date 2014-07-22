from django.http import HttpResponse
from django.contrib import auth

def register(request):
    pass

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponse("OK")
    else:
        return HttpResponse("ERROR")

def logout(request):
    auth.logout(request)
    return HttpResponse("LOGGED OUT")
