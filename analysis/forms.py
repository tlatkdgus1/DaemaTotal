from django import forms
from .models import VirusModel

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = VirusModel
        fields = ('file',)
        labels = {
            'file': 'Upload',
        }