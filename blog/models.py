# -*- coding:utf-8 -*-
from django.db import models

from prk.account.models import Account
from prk.pm.project.models import Project
from prk.utils.models import Titled, BaseModel


class Post(BaseModel):
    brief = models.TextField(verbose_name=u"توضیح اولیه", null=True, blank=True)
    desc = models.TextField(verbose_name=u"ادامه مطلب", null=True, blank=True)
    active = models.BooleanField(verbose_name=u"فعال", default=True)
    publish_date = models.DateTimeField(verbose_name=u"تاریخ انتشار", null=True, blank=True)

    class Meta:
        verbose_name = u"پست"
        verbose_name_plural = u"پست ها"


class ContentNews(BaseModel):
    brief = models.TextField(verbose_name=u"توضیح اولیه", null=True, blank=True)
    desc = models.TextField(verbose_name=u"ادامه مطلب", null=True, blank=True)
    active = models.BooleanField(verbose_name=u"فعال", default=True)
    publish_date = models.DateTimeField(verbose_name=u"تاریخ انتشار", null=True, blank=True)

    class Meta:
        verbose_name = u"مطلب"
        verbose_name_plural = u"مطلب ها"
