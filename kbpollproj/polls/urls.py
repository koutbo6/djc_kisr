from django.conf.urls import url
from polls import views

urlpatterns = [
    url(r'^list/', views.PollList.as_view(), name='poll_list',),
    url(r'^poll/(?P<poll_id>\d+)/$', views.PollDetails.as_view(), name='poll_details',),
    url(r'^poll/(?P<poll_id>\d+)/response/$', views.poll_response, name='poll_response',),
    url(r'^poll/create/$', views.poll_create, name='poll_create',),
    url(r'^poll/(?P<poll_id>\d+)/edit/$', views.poll_edit, name='poll_edit',),
    url(r'^user/(?P<user_id>\d+)/list/$', views.UserPollList.as_view(), name='user_polls',),
]
