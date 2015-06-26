# -*- coding:utf-8 -*-
from django.db import models
# from taggit.managers import TaggableManager


class Named(models.Model):
    name = models.CharField(verbose_name=u"نام", max_length=500)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class Titled(models.Model):
    title = models.CharField(verbose_name=u"عنوان", max_length=255)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class BaseModel(Titled):
    created_on = models.DateTimeField(verbose_name=u"تاریخ ایجاد", auto_now_add=True)
    creator = models.ForeignKey('account.Account', verbose_name=u"سازنده", null=True, blank=True, related_name='income_creators')
    # category = models.ForeignKey('categories.Category', verbose_name=u"دسته بندی", null=True, blank=True)
    # tags = TaggableManager()
