from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.views.generic.edit import CreateView
from class_based_auth_views.views import LogoutView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from datetime import datetime
from class_based_auth_views.views import LoginView
from .forms import UserCreateForm, UserEditForm, UserAuthenticationForm


class EditUserView(View):
    form_class = UserEditForm
    template_name = 'usermanagement/user_edit_screen.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class(instance=request.user)
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
        return redirect(reverse('home'))

    def get_context_data(self, **kwargs):
        context = {}
        context["action"] = reverse('edit_user')
        context["submit_text"] = "Lagre"
        return context


class UserCreateView(CreateView):
    template_name = "usermanagement/register_screen.html"
    model = User
    form_class = UserCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_date = datetime.now()
        form.save()
        return super(UserCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context["action"] = reverse('register')
        context["submit_text"] = "Registrer"
        return context

    def get_success_url(self):
        return reverse('login')


class UserLoginView(LoginView):
    template_name = "usermanagement/login_screen.html"
    form_class = UserAuthenticationForm

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context["action"] = reverse('login')
        context["submit_text"] = "logg inn"
        return context


class UserLogoutView(LogoutView):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated():
            return redirect(reverse('login'))
        return redirect(self.get_redirect_url())

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(self.request)

        return redirect(self.get_redirect_url())

    def get_redirect_url(self):
        return reverse('login')


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
