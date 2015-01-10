from django.shortcuts import render
from courses.models import Course
from newsfeed.models import NewsItem
from .models import Sponsor


def frontpage(request):
    context = {}
    courses = Course.objects.open_verbose()
    sponsors = Sponsor.objects.all()

    if(request.user.is_authenticated()):
        for course in courses:
            course.signed_up = \
                course.registrations.filter(pk=request.user.id).count()

    context['newsitems'] = NewsItem.objects.all().order_by('-time_stamp')[:5]
    context['courses'] = courses
    context['header'] = "Kodeklubben Trondheim"
    context['sponsors'] = sponsors
    return render(request, 'frontpage/frontpage.html', context)
