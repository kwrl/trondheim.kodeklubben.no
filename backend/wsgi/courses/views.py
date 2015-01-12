from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from .models import \
    Course, Registration, Task, TaskSubmission, ScoreProfile
from .forms import TaskSubmissionForm


class CourseListView(View):
    template_name = 'courses/course_select.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {
            'courses': request.user.course_set.all(),
            'profile': ScoreProfile.get_score_profile(request.user),
            'highscore': ScoreProfile.objects.all().order_by('-score')[:10]
        }
        return render(request,
                      self.template_name,
                      context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        pass


class ProfileView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {}
        profile = ScoreProfile.get_score_profile(request.user)
        context['username'] = request.user.username
        context['rank'] = profile.current_rank
        context['score'] = profile.score
        context['courses'] = request.user.course_set.all()
        context['valid_submissions'] = \
            TaskSubmission.objects.filter(submitted_by=request.user,
                                          valid=True).values_list('task',
                                                                  flat=True)

        return render(request, 'courses/profile.html', context)


class TaskSubmissionView(View):
    form_class = TaskSubmissionForm
    template_name = 'courses/task.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class()
        context['subs'] = TaskSubmission.objects.filter(
            submitted_by=request.user,
            task=self.kwargs['task_id']
        )
        context['valid_subs'] = context['subs'].filter(
            valid=True
        )
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
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = {}
        context['task'] = Task.objects.get(pk=self.kwargs['task_id'])
        return context


class CourseRegistrationView(View):
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        course_id = request.POST['course_id']
        course = Course.objects.get(pk=course_id)

        if course:
            Registration.objects.filter(user=request.user,
                                        course=course).delete()
        else:
            return

        if request.POST['sign_up'] == u'master':
            Registration(user=request.user,
                         course=course,
                         granted=False,
                         code_master=True,
                         role=Registration.CODE_MASTER).save()

        elif request.POST['sign_up'] == u'kid':
            Registration(user=request.user,
                         course=course,
                         granted=False,
                         code_master=False,
                         role=Registration.KID).save()

        elif request.POST['sign_up'] == u'reserve':
            Registration(user=request.user,
                         course=course,
                         granted=False,
                         code_master=False,
                         role=Registration.RESERVE).save()
        return
