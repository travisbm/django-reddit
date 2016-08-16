from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    post_text  = models.CharField(max_length=500)
    pub_date   = models.DateTimeField('date published')
    up_votes   = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)

