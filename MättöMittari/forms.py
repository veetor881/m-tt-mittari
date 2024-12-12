from django import forms
from .models import Ruoka, Arvio

class ArvioForm(forms.ModelForm):
    class Meta:
        model = Arvio
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}