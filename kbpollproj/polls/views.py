from django.shortcuts import render
from django.http import Http404
from .models import Poll


def poll_list(request):
    # construct a queryset
    qs = Poll.objects.all()
    return render(request, "poll_list.html", {"polls": qs})


def poll_details(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, "poll_details.html", {"poll": poll})
