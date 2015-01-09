from django.forms.widgets import ClearableFileInput
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from .models import TaskSubmission
from django.forms import ModelForm
import os


class FileInputInitial(ClearableFileInput):
    initial_text = 'Last uploaded'
    input_text = 'Change'
    clear_checkbox_label = 'Clear'
    template_with_initial = \
        '%(initial_text)s: %(initial)s <br />%(input_text)s: %(input)s'
    url_markup_template = '{0}'

    def render(self, name, value, attrs=None):
        substitutions = {
            'initial_text': self.initial_text,
            'input_text': self.input_text,
        }
        template = '%(input)s'
        substitutions['input'] = \
            super(ClearableFileInput, self).render(name, value, attrs)

        if value and hasattr(value, "url"):
            template = self.template_with_initial
            substitutions['initial'] = \
                force_text(os.path.split(os.path.abspath(value.path))[1])
        return mark_safe(template % substitutions)


class TaskSubmissionForm(ModelForm):
    class Meta:
        model = TaskSubmission
        fields = ['content_file']
        labels = {'content_file': ('Last opp fil')}
        widgets = {'content_file': FileInputInitial(), }

    def save(self):
        sub = TaskSubmission()
        sub.task = self.instance.task
        sub.content_file = self.cleaned_data.get('content_file')
        sub.submitted_by = self.instance.submitted_by
        sub.valid = self.instance.valid
        sub.status = TaskSubmission.NOT_EVALUATED
        sub.save()
