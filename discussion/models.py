# -*- coding:utf-8 -*-
from django.db import models

from prk.account.models import Account
from prk.pm.project.models import Project
from prk.utils.models import Titled, BaseModel


class Discussion(BaseModel):
    desc = models.TextField(verbose_name=u"توضیح اولیه", null=True, blank=True)
    record = models.TextField(verbose_name=u"صورت جلسه", null=True, blank=True)
    is_meet = models.BooleanField(verbose_name=u"جلسه است", default=True)

    class Meta:
        verbose_name = u"گفتمان"
        verbose_name_plural = u"گفتمان ها"


class Speech(models.Model):
    discussion = models.ForeignKey(Discussion, verbose_name=u"گفتمان مربوط")
    desc = models.TextField(verbose_name=u"متن", null=True)
    person = models.ForeignKey(Account, verbose_name=u"گوینده", null=True, blank=True)
    created_on = models.DateTimeField(verbose_name=u"تاریخ ایجاد", auto_now_add=True)

    class Meta:
        verbose_name = u"گفتار"
        verbose_name_plural = u"گفتار ها"

