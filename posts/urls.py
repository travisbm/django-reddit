from django.conf.urls import url

from . import views

app_name = 'posts'
urlpatterns =[
    url(r'^$', views.index, name='index'),
    # ex: /posts/new
    url(r'^new/$', views.post_new, name='post_new'),
    # ex: /posts/5/vote/
    url(r'^(?P<post_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /posts/5/
    url(r'^(?P<post_id>[0-9]+)/$', views.post, name='post'),
]
