from django.forms import ModelForm, FileField
from .models import Registration, Course, Task, TaskSubmission

class TaskSubmissionForm(ModelForm):
    class Meta:
        model = TaskSubmission
        fields = ['content_file']
        labels = { 'content_file': ('Last opp fil') }


