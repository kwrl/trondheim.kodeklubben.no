from django.views.generic import View
from django.shortcuts import render
from newsfeed.models import NewsItem
from courses.models import Course
from .models import Sponsor


class FrontpageView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        courses = Course.objects.open_registration()
        sponsors = Sponsor.objects.all()

        if(request.user.is_authenticated()):
            for course in courses:
                course.signed_up = \
                    course.registrations.filter(pk=request.user.id).exists()

        context['newsitems'] = \
            NewsItem.objects.filter(hide=False).order_by('-time_stamp')[:5]
        context['courses'] = courses
        context['header'] = "Kodeklubben Trondheim"
        context['sponsors'] = sponsors
        return render(request, 'frontpage/frontpage.html', context)


