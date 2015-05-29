from django import forms
from django.forms.models import inlineformset_factory
from .models import Response, Poll, Choice


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'
        widgets = {
            'choice': forms.RadioSelect,
        }


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = '__all__'


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'


InlineChoiceFormSet = inlineformset_factory(
        Poll,
        Choice,
        fields='__all__',
        can_delete=False,
        extra=10,
        max_num=10,
    )
