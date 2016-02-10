# -*- coding:utf-8 -*-
from django.db import models

from account.models import Account
from utils.models import LogModel, BaseModel


class BankAccount(BaseModel):
    account_num = models.CharField(verbose_name="شماره حساب", null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = u"حساب"
        verbose_name_plural = u"حساب ها"


class Transaction(LogModel):
    PAY_TYPE = (
        (1, 'برداشت'),
        (2, 'واریز'),
    )
    pay_type = models.IntegerField(verbose_name="نوع پرداخت", choices=PAY_TYPE)

    MONEY_TYPE = (
        (1, 'حقوق'),
        (2, 'تنخواه'),
    )
    money_type = models.IntegerField(verbose_name="نوع پرداخت", choices=MONEY_TYPE)

    desc = models.TextField(verbose_name=u"توضیحات", null=True, blank=True)

    code = models.CharField(verbose_name="شماره سند", null=True, blank=True, max_length=255)

    amount = models.BigIntegerField(verbose_name=u"مبلغ(تومان)", default=0)
    person = models.ForeignKey(Account, verbose_name=u"شخص", null=True, blank=True,
                               related_name='persons')
    date = models.DateField(verbose_name="تاریخ", null=True, blank=True)

    bank_account = models.ForeignKey('BankAccount', related_name='transactions')
    # tags = models.ManyToManyField(Tag)
    # project = models.ForeignKey(Project, verbose_name=u"پروژه", null=True, blank=True)

    class Meta:
        verbose_name = u"تراکنش"
        verbose_name_plural = u"تراکنش ها"

    @property
    def income(self):
        return self.amount if self.pay_type == 1 else 0

    @property
    def payment(self):
        return self.amount if self.pay_type == 2 else 0
