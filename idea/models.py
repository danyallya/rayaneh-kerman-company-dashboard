# -*- coding:utf-8 -*-
from django.db import models

from account.models import Account
from pm.models import Project
from utils.models import Titled, BaseModel


class IdeaState(Titled):
    class Meta:
        verbose_name = u"وضعیت ایده"
        verbose_name_plural = u"وضعیت های ایده"


class Idea(BaseModel):
    brief = models.TextField(verbose_name=u"توضیح مختصر", null=True, blank=True)
    first_desc = models.TextField(verbose_name=u"توضیحات ایده خام", null=True, blank=True)
    economic_justification = models.TextField(verbose_name=u"توجیه اقتصادی", null=True, blank=True)
    project = models.ForeignKey(Project, verbose_name=u"پروژه", null=True, blank=True)
    state = models.ForeignKey(IdeaState, verbose_name=u"وضعیت", null=True, blank=True)

    class Meta:
        verbose_name = u"ایده"
        verbose_name_plural = u"ایده ها"
