from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    post_text  = models.CharField(max_length=500)
    pub_date   = models.DateTimeField('date published')
    votes   = models.IntegerField(default=0)

    def __str__(self):
      return self.post_text
