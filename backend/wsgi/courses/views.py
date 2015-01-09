from django.http.response import HttpResponse
from django.shortcuts import render
from  django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from .models import \
    Course, Registration, Task, TaskSubmission, get_score_profile
from .forms import TaskSubmissionForm


class CourseListView(View):
    template_name = 'courses/course_select.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request,
                      self.template_name,
                      {'courses': Course.objects.all()})


    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        pass

@login_required
def view_profile(request):
    context = {}
    profile = get_score_profile(request.user)
    context['username'] = request.user.username
    context['rank'] = profile.current_rank
    context['score'] = profile.score
    context['courses'] = request.user.course_set.all()
    context['valid_submissions'] = \
        TaskSubmission.objects.filter(submitted_by=request.user,
                                      valid=True).values_list('task', flat=True)

    return render(request, 'courses/profile.html', context)


class TaskSubmissionView(View):
    form_class = TaskSubmissionForm
    template_name = 'courses/task.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class()
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=self.kwargs['task_id'])
        sub = TaskSubmission()
        sub.task = task
        sub.submitted_by = request.user
        sub.valid = False
        form = self.form_class(request.POST, request.FILES, instance=sub)
        if form.is_valid():
            form.save()
        context = self.get_context_data()
        context['form'] = self.form_class()
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {}
        context['task'] = Task.objects.get(pk=self.kwargs['task_id'])
        return context


def list_courses(request):
    queryset = Course.objects.all()

    for course in queryset:
        course.taken = Registration.objects.filter(course=course).count()

    if(request.user.is_authenticated()):
        for course in queryset:
            course.signed_up = \
                course.registrations.filter(user=request.user).count()

    context = {}
    context['courses'] = queryset
    return render(request, 'courses/courses.html', context)


@login_required
def register(request):
    if request.method != 'POST':
        return HttpResponse("Det er ikke noe spennende her.")

    course_id = request.POST['course_id']

    master = request.POST['sign_up'] == u'master'
    kid = request.POST['sign_up'] == u'kid'
    off = request.POST['sign_up'] == u'off'

    course = Course.objects.get(pk=course_id)

    if not course:
        return

    if master:
        Registration.objects.filter(user=request.user, course=course).delete()
        Registration(user=request.user,
                     course=course,
                     granted=False,
                     code_master=True).save()
        return

    if kid:
        Registration.objects.filter(user=request.user, course=course).delete()
        Registration(user=request.user,
                     course=course,
                     granted=False,
                     code_master=False).save()
        return

    if off:
        Registration.objects.filter(user=request.user, course=course).delete()
