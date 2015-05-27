from django.conf.urls import url
from polls import views

urlpatterns = [
    url(r'^list/', views.PollList.as_view(), name='poll_list',),
    url(r'^poll/(?P<poll_id>\d+)/$', views.PollDetails.as_view(), name='poll_details',),
    url(r'^poll/(?P<poll_id>\d+)/response/$', views.poll_response, name='poll_response',),
]
