#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from fandjango.models import User



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

@receiver(post_save, sender=User)
def pages_save(sender, instance, created, **kwargs):
    facebook_user = sender
    if created:
        pages = [account for account in graph.get('me/accounts').get('data') \
                if account.get('category') != u'Application']
        for page in pages:
            page_obj = Page(
                facebook_user   = facebook_user,
                facebook_id     = page.id,
                name            = page.name,
                access_token    = page.access_token,
                category        = page.category
            )
            page_obj.save()