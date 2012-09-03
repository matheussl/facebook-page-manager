#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _



class UserProfile(models.Model):
    class Meta:
        verbose_name = _('UserProfile')
        verbose_name_plural = _('UserProfiles')

    def __unicode__(self):
        pass
    
    user = models.OneToOneField('auth.User', verbose_name=_('user'))
    facebook_users = models.ForeignKey('fandjango.User')


class Post(models.Model):
    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __unicode__(self):
        pass
    
    facebook_user = models.ForeignKey('fandjango.User')
    text = models.TextField()
    image = models.ImageField(upload_to='post/')
    link = models.URLField()
    page = models.ForeignKey('core.Page')


class Page(models.Model):
    class Meta:
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')

    def __unicode__(self):
        pass
    
    facebook_user = models.ForeignKey('fandjango.User')
    facebook_id = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    access_token = models.CharField(max_length=300)
    category = models.CharField(max_length=100)
