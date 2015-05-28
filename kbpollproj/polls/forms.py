from django import forms
from .models import Response, Choice


class ResponseForm(forms.ModelForm):
    choice = forms.ModelChoiceField(
        queryset=Choice.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None)
        
    class Meta:
        model = Response
        fields = '__all__'
