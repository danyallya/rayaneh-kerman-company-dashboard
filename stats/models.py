# -*- coding:utf-8 -*-
from django.db import models

from product.models import ProductVersion


class AppSignal(models.Model):
    product_version = models.ForeignKey(ProductVersion, verbose_name=u"محصول", on_delete=models.CASCADE,
                                        related_name='app_signal')
    created_on = models.DateTimeField(verbose_name=u"تاریخ ایجاد", auto_now_add=True)
    code = models.CharField(verbose_name=u"کد", null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = u"سیگنال"
        verbose_name_plural = u"سیگنال ها"
