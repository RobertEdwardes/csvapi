from django import forms
from django.forms.widgets import ClearableFileInput
from .models import main_table

class UploadCsv(forms.Form):
    file = forms.FileField()