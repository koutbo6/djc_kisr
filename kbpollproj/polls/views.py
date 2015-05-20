from django.shortcuts import render
from .models import Poll


def poll_list(request):
    # construct a queryset
    qs = Poll.objects.all()
    return render(request, "poll_list.html", {"polls": qs})
