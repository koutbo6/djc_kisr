from django.contrib import admin
from .models import Poll, Choice, Response


class PollAdmin(admin.ModelAdmin):
    # Fields to show in list view
    list_display = ('name', 'category', 'question', )

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Response)
