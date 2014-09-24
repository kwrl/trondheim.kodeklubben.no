from django.forms import ModelForm
from .models import Registration, Course, Task, TaskSubmission

class TaskSubmissionForm(ModelForm):
    class Meta:
        model = TaskSubmission
        fields = ['content_file']


