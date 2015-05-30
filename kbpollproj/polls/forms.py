from django import forms
from django.forms.models import inlineformset_factory
from .models import Response, Poll, Choice, UserProfile


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


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def signup(self, request, user):
        # create user profile here
        UserProfile.objects.create(
            user=user,
            gender=self.cleaned_data.get('gender'),
            bio=self.cleaned_data.get('bio'),
            location=self.cleaned_data.get('location'),
            phone=self.cleaned_data.get('phone'),
        )
