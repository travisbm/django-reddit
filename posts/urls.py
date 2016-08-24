from django.conf.urls import url

from . import views

app_name = 'posts'
urlpatterns =[
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/vote/
    url(r'^(?P<post_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^new/$', views.post_new, name='post_new'),
]
