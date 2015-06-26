# -*- coding:utf-8 -*-
from django.db import models
from model_utils.managers import InheritanceManager

from prk.account.models import Account
from prk.pm.project.models import Project
from prk.utils.models import Titled, BaseModel


class BankAccount(Titled):
    class Meta:
        verbose_name = u"درآمد"
        verbose_name_plural = u"درآمد ها"


class Transaction(BaseModel):
    amount = models.BigIntegerField(verbose_name=u"مبلغ(تومان)", default=0)
    payer = models.ForeignKey(Account, verbose_name=u"پرداخت کننده", null=True, blank=True,
                              related_name='income_payers')
    desc = models.TextField(verbose_name=u"توضیحات", null=True, blank=True)
    project = models.ForeignKey(Project, verbose_name=u"پروژه", null=True, blank=True)

    objects = InheritanceManager()

    class Meta:
        verbose_name = u"تراکنش"
        verbose_name_plural = u"تراکنش ها"


class Income(Transaction):
    class Meta:
        verbose_name = u"درآمد"
        verbose_name_plural = u"درآمد ها"


class Payment(Transaction):
    receiver = models.ForeignKey(Account, verbose_name=u"دریافت کننده", null=True, blank=True,
                                 related_name='payment_receivers')

    class Meta:
        verbose_name = u"پرداخت"
        verbose_name_plural = u"پرداخت ها"


