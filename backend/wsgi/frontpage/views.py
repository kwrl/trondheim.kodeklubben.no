from django.shortcuts import render
from courses.models import get_registered_kids
from newsfeed.models import NewsItem

def frontpage(request):
    context = {}
    courses = get_registered_kids()

    if(request.user.is_authenticated()):
        for course in courses:
            course.signed_up = course.registrations.filter(pk=request.user.id).count()

    context['newsitems'] = NewsItem.objects.all().order_by('-time_stamp')
    context['courses'] = courses 
    context['header'] = "Kodeklubben Trondheim"
    return render(request,'frontpage/frontpage.html', context)
