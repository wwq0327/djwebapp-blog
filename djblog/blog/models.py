# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(u'文章分类', max_length=64)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('category', (), {'pk': self.pk})
    
class Post(models.Model):
    title = models.CharField(u"标题", max_length=128)
    author = models.ForeignKey(User)
    po_type = models.ForeignKey(Category, verbose_name=u'文章分类', blank=True, null=True)
    content = models.TextField(u"内容")
    pub_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]

    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {'pk': self.pk}) 
