from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from .forms import UserCreateForm

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
