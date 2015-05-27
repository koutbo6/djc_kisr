from django import forms
from .models import Choice


class ResponseForm(forms.Form):
    # We will set the choice to all objects now
    # but we will filter it in the view to
    # show choices for out Poll only
    choice = forms.ModelChoiceField(
        queryset=Choice.objects.all(),
        widget=forms.RadioSelect,
        )
    comment = forms.CharField(widget=forms.Textarea)
