from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Poll


class PollList(ListView):
    model = Poll
    template_name = "poll_list.html"
    context_object_name = "polls"


class PollDetails(DetailView):
    model = Poll
    template_name = "poll_details.html"
    context_object_name = "poll"
    pk_url_kwarg = "poll_id"
