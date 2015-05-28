from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Poll, Choice
from .forms import ResponseForm

class PollList(ListView):
    model = Poll
    template_name = "poll_list.html"
    context_object_name = "polls"


class PollDetails(DetailView):
    model = Poll
    template_name = "poll_details.html"
    context_object_name = "poll"
    pk_url_kwarg = "poll_id"


def poll_response(request, poll_id):
    # get the poll object
    poll = get_object_or_404(Poll, pk=poll_id)

    # check if user is posting data
    if request.method == 'POST':
        # then create a bounded form
        form = ResponseForm(request.POST)
        # validate the data
        if form.is_valid():
            # we now have validated data incleaned_data
            # get the respondent choice object
            r_choice = form.cleaned_data['choice']
            # get the respondent comment
            r_comment = form.cleaned_data['comment']

            # create the new response entry
            # We can do it in our choice reverse relation
            r_choice.response_set.create(
                comment=r_comment,
            )

            # success message
            messages.success(request, 'Your response was successfully posted.')

            # now redirect to poll list
            return redirect('poll_list')

    # If not Post, meaning
    # the user opened this view for first time
    else:
        # then present an unbound form
        form = ResponseForm()
        # filter options for choice
        # display only ones for current poll
        form.fields['choice'].queryset = Choice.objects.filter(poll=poll)

    return render(
        request,
        'poll_response.html',
        {
            'poll': poll,
            'form': form,
        }
    )
