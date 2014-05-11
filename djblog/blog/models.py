# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(u"标题", max_length=128)
    author = models.ForeignKey(User)
    content = models.TextField(u"内容")
    pub_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]

    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {'pk': self.pk}) 
