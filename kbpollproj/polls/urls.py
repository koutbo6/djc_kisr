from django.conf.urls import patterns, url
# import the views module
# this was not needed Django pre-1.8
from polls import views

urlpatterns = [
    url(r'^list/', views.poll_list, name='poll_list',),
]

# This is how to do it in Django pre-1.8
# urlpatterns = patterns('polls.views',
#     url(r'^list/', 'poll_list', name='poll_list',),
# )
