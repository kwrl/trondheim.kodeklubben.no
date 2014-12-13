from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import NewsItem

class NewsItemForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = NewsItem
