from django.forms import ModelForm
from .models import Course

class CourseAdminForm(ModelForm):
    class Meta:
        model = Course
        exclude = ('',)
