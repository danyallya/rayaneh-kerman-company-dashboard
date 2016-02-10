# -*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import BaseModel


class Project(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    summary = models.TextField(_(u'Summary'), null=True, blank=True)
    responsible = models.ForeignKey('account.Account', verbose_name=_(u'Responsible'), null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)

    class Meta:
        ordering = ['-entry_date']
        app_label = 'pm'

    def __str__(self):
        return self.title


class TimeSpend(BaseModel):
    # issue = models.ForeignKey(Issue, null=True, blank=True)
    account = models.ForeignKey('account.Account', verbose_name=u"واگذارشده به", related_name='assignes')
    project = models.ForeignKey(Project, null=True, blank=True)
    due_date = models.DateField(u"زمان", null=True)
    desc = models.TextField(verbose_name=u"توضیح", null=True)
    # progress = models.IntegerField(verbose_name=u"درصد انجام", default=0)
    time_spend = models.FloatField(u'زمان گذاشته شده', null=True)

    class Meta:
        app_label = 'pm'
        verbose_name = "زمان"
        verbose_name_plural = "زمان ها"


class WorkItem(BaseModel):
    account = models.ForeignKey('account.Account', verbose_name=u"واگذارشده به", related_name='work_items')
    project = models.ForeignKey(Project, null=True, blank=True)
    due_date = models.DateField("زمان انجام", null=True)
    desc = models.TextField(verbose_name=u"توضیح", null=True)
    progress = models.IntegerField(verbose_name=u"درصد انجام", default=0)

    class Meta:
        app_label = 'pm'
        verbose_name = "کار"
        verbose_name_plural = "کارها"
