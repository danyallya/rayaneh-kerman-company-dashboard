# -*- coding:utf-8 -*-
from django.conf import settings
from django.db import models

from prk.account.models import Account
from prk.pm.project.models import Project, ProjectVersion
from prk.utils.models import Titled, BaseModel


class Product(BaseModel):
    project = models.ForeignKey(Project, verbose_name=u"پروژه", null=True, blank=True)
    active = models.BooleanField(verbose_name=u"فعال", default=True)
    desc = models.TextField(verbose_name=u"توضیح", null=True, blank=True)
    name = models.CharField(verbose_name=u"مشخصه", max_length=255)

    class Meta:
        verbose_name = u"محصول"
        verbose_name_plural = u"محصول ها"


class ProductVersion(BaseModel):
    icon = models.ImageField(verbose_name=u"آیکن", upload_to="product_icon", null=True, blank=True)
    project_version = models.ForeignKey(ProjectVersion, verbose_name=u"پروژه", null=True, blank=True)
    product = models.ForeignKey(Product, verbose_name=u"محصول", null=True, blank=True)
    changes = models.TextField(verbose_name=u"تغییرات", null=True, blank=True)
    code = models.CharField(verbose_name=u"کد", null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = u"محصول"
        verbose_name_plural = u"محصول ها"


class ProductLink(models.Model):
    link = models.URLField(verbose_name=u"لینک")
    product = models.ForeignKey(Product, verbose_name=u"محصول", null=True, on_delete=models.CASCADE,
                                related_name='product_links')

    class Meta:
        verbose_name = u"لینک محصول"
        verbose_name_plural = u"لینک های محصول"


class ProductImage(models.Model):
    image = models.ImageField(verbose_name=u"تصویر", upload_to="product_images")
    product = models.ForeignKey(Product, verbose_name=u"محصول", null=True, on_delete=models.CASCADE,
                                related_name='product_images')

    class Meta:
        verbose_name = u"تصویر محصول"
        verbose_name_plural = u"تصاویر محصول"

    def __unicode__(self):
        return self.image.url

    @property
    def image_url(self):
        return settings.SITE_URL + self.image.url
