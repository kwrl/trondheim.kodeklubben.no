from rest_framework import status, viewsets, permissions
from django.http.response import HttpResponse
from rest_framework.decorators import api_view, action, link
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .serializers import CourseHeaderSerializer, CourseFullSerializer 
from .models import Course, Registration, ScoreProfile, Ranking

def list_courses(request):
    queryset = Course.objects.all()

    for course in queryset:
        course.taken = Registration.objects.filter(course=course).count()

    if(request.user.is_authenticated()):
        for course in queryset:
            course.signed_up = course.registrations.filter(user=request.user).count()
    

    context = {}

    context['courses'] = queryset

    return render(request, 'courses/courses.html',context)


@login_required
def register(request):
    if request.method!='POST':
        return HttpResponse("Det er ikke noe spennende her.")

    course_id = request.POST['course_id']
    user_id = request.user.id

    master  = request.POST['sign_up']==u'master'
    kid     = request.POST['sign_up']==u'kid'
    off     = request.POST['sign_up']==u'off'

    course = Course.objects.get(pk=course_id)

    if not course:
        return

    if master:
        Registration.objects.filter(user=request.user, course=course).delete()
        Registration(user=request.user, course=course, granted=False, code_master=True).save()
        return

    if kid:
        Registration.objects.filter(user=request.user, course=course).delete()
        Registration(user=request.user, course=course, granted=False, code_master=False).save()
        return

    if off:
        Registration.objects.filter(user=request.user, course=course).delete()

@login_required
def view_profile(request):
    profile = ScoreProfile.objects.filter(user=request.user).first()

    if not profile:
        rank = Ranking.objects.all().order_by("-required_score")[0]
        profile = ScoreProfile(user=request.user, score=0, current_rank=rank)
        profile.save()

    return HttpResponse(profile.current_rank.name)

@login_required
def list_tasks(request):
    pass
