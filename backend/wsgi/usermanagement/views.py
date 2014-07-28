from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def register(request):
    pass

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("LOGGED IN")
        else:
            return HttpResponse("USER NOT ACTIVE")
    else:
        return HttpResponse("NO SUCH USER")

def logout(request):
    auth.logout(request)
    return HttpResponse("LOGGED OUT")
