# -*- coding:utf-8 -*-
from django.db import models
# from taggit.managers import TaggableManager


class Named(models.Model):
    name = models.CharField(verbose_name=u"نام", max_length=500)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Titled(models.Model):
    title = models.CharField(verbose_name=u"عنوان", max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class LogModel(models.Model):
    creator = models.ForeignKey('account.Account', verbose_name="سازنده", null=True, blank=True)
    created_on = models.DateTimeField(verbose_name="تاریخ ایجاد", auto_now_add=True)

    class Meta:
        abstract = True


class BaseModel(Titled, LogModel):
    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def update(self):
        pass
