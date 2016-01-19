# -*- coding:utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import UserManager, AbstractUser
from model_utils.managers import InheritanceManager
from account.permissions import Permission, PERMISSION_TYPE


class AccountRole(models.Model):
    name = models.CharField("نام", max_length=128)

    class Meta:
        app_label = 'account'
        verbose_name_plural = 'نقش ها'
        verbose_name = 'نقش'

    def __str__(self):
        return self.name


class AccountPermission(models.Model):
    perm = models.IntegerField(verbose_name="ماژول", choices=Permission.get_permission_choices())
    perm_type = models.IntegerField(verbose_name="نوع", choices=PERMISSION_TYPE)

    role = models.ForeignKey(AccountRole, verbose_name="نقش", related_name='perms')

    class Meta:
        app_label = 'account'
        verbose_name_plural = 'اجازه ها'
        verbose_name = 'اجازه'

    def __str__(self):
        return self.role.name + " - " + self.get_perm_display() + " - " + self.get_perm_type_display()


class AccountTeam(models.Model):
    name = models.CharField(_(u'Role'), max_length=128)

    class Meta:
        app_label = 'account'

    def __str__(self):
        return self.name


class AccountManager(UserManager, InheritanceManager):
    pass
    # def create_user(self, username, email, first_name, last_name, password=None):
    #     if not email:
    #         raise ValueError('Users must have an email address')
    #
    #     user = self.model(email=AccountManager.normalize_email(email))
    #     user.first_name = first_name
    #     user.last_name = last_name
    #     user.username = username
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user
    #
    # def create_superuser(self, username, email, first_name, last_name, password):
    #     u = self.create_user(username=username, email=email, first_name=first_name,
    #                          last_name=last_name, password=password)
    #     u.is_admin = True
    #     u.save(using=self._db)
    #     return u


class BaseAccount(AbstractUser):
    ACCOUNT_TYPES = (
        ('AD', 'Admin'),
        ('US', 'User'),
    )
    role = models.ForeignKey(AccountRole, verbose_name='نقش', null=True)
    team = models.ForeignKey(AccountTeam, verbose_name=_(u'Team'), null=True, blank=True)
    type = models.CharField(_(u'Account Type'), max_length=4, choices=ACCOUNT_TYPES, default='US')
    follows = models.ManyToManyField('self', related_name='followers', symmetrical=False, blank=True)
    phone = models.CharField(_(u'Phone'), max_length=30, null=True, blank=True)
    im = models.CharField(_(u'IM'), max_length=255, null=True, blank=True)
    website = models.CharField(_(u'Website'), max_length=1024, null=True, blank=True)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        app_label = 'account'


class Account(BaseAccount):
    description = models.TextField(verbose_name=u"توضیحات", null=True, blank=True)
    image = models.ImageField(verbose_name=u"تصویر", upload_to="account_image", null=True)
    objects = AccountManager()

    class Meta:
        app_label = 'account'
        verbose_name_plural = "کاربران"
        verbose_name = "کاربر"


class Filter(models.Model):
    name = models.CharField(_(u'Filter Name'), max_length=128)
    query = models.CharField(_(u'Filter Query'), max_length=1024)

    class Meta:
        app_label = 'account'

    def __str__(self):
        return self.name


class FavoriteFilters(models.Model):
    account = models.ForeignKey(Account, verbose_name=_(u'Account'))
    filters = models.ManyToManyField(Filter, verbose_name=_(u'Filters'))

    class Meta:
        app_label = 'account'


class AccountImage(models.Model):
    image = models.ImageField(verbose_name=u"تصویر", upload_to="account_extra_images")
    account = models.ForeignKey(Account, verbose_name=_(u'Account'), on_delete=models.CASCADE,
                                related_name='extra_images')

    class Meta:
        app_label = 'account'

    def __str__(self):
        return self.image.url

    @property
    def image_url(self):
        return settings.SITE_URL + self.image.url


class OtherProject(models.Model):
    account = models.OneToOneField(BaseAccount, verbose_name=_(u'Account'), related_name='projects')
    name = models.CharField(verbose_name=u"نام", max_length=255, null=True, blank=True)

    class Meta:
        app_label = 'account'


class AccountLink(models.Model):
    account = models.OneToOneField(Account, verbose_name=_(u'Account'), related_name='links')
    name = models.CharField(verbose_name=u"نام", max_length=255, null=True, blank=True)

    class Meta:
        app_label = 'account'


class RelationAccount(BaseAccount):
    description = models.TextField(verbose_name=u"توضیحات", null=True, blank=True)

    class Meta:
        app_label = 'account'
