from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg

from .models import Poll, Choice
from .forms import ResponseForm, PollForm, InlineChoiceFormSet


class PollList(ListView):
    model = Poll
    template_name = "poll_list.html"
    context_object_name = "polls"
    queryset = Poll.objects.annotate(
        total_choices=Count('choice', distinct=True),
        total_responses=Count('choice__response'),
    )

    def get_context_data(self, **kwargs):
        # run super implementation of method to get context
        context = super().get_context_data(**kwargs)
        # now add to it
        stats = {}
        stats["total_polls"] = self.queryset.count()
        # will add avg_choices and avg_responses to stats
        stats.update(
            self.queryset.aggregate(
                avg_choices=Avg('total_choices'),
                avg_responses=Avg('total_responses')
            )
        )
        # add stats to the context
        context["stats"] = stats
        # do not forget to return the context
        return context


class PollDetails(DetailView):
    model = Poll
    template_name = "poll_details.html"
    context_object_name = "poll"
    pk_url_kwarg = "poll_id"


@login_required
def poll_response(request, poll_id):
    # get the poll object
    poll = get_object_or_404(Poll, pk=poll_id)

    # check if user is posting data
    if request.method == 'POST':
        # then create a bounded form
        form = ResponseForm(request.POST)
        # validate the data
        if form.is_valid():
            form.save()
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


@login_required
def poll_create(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False)
            formset = InlineChoiceFormSet(request.POST, instance=poll)
            if formset.is_valid():
                poll.save()
                formset.save()
                messages.success(request, 'Poll was successfully created.')
                return redirect('poll_list')
    else:
        form = PollForm()
        formset = InlineChoiceFormSet(instance=Poll())
    return render(
        request,
        'poll_create.html',
        {
            "form": form,
            "formset": formset,
        }
    )


@login_required
def poll_edit(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id, author=request.user)

    # enable ability to delete choices
    InlineChoiceFormSet.can_delete = True

    if request.method == 'POST':
        form = PollForm(request.POST, instance=poll)
        if form.is_valid():
            formset = InlineChoiceFormSet(request.POST, instance=poll)
            if formset.is_valid():
                form.save()  # this will update object
                formset.save()  # this will update objects
                messages.success(request, 'Poll was successfully edited.')
                return redirect('poll_list')
    else:
        # both form and formset are bound to
        # the poll object we are editing
        form = PollForm(instance=poll)
        formset = InlineChoiceFormSet(instance=poll)
    return render(
        request,
        'poll_edit.html',
        {
            "poll": poll,
            "form": form,
            "formset": formset,
        }
    )


class UserPollList(ListView):
    model = Poll
    template_name = "poll_list.html"
    context_object_name = "polls"

    def get_queryset(self):
        return Poll.objects.filter(author=self.kwargs["user_id"])
