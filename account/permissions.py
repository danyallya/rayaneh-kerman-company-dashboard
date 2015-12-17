from django.core.urlresolvers import reverse

from django.http.response import HttpResponseForbidden

from pm.models import TimeSpend

__author__ = 'M.Y'

SELF_ACCESS = 1
FULL_ACCESS = 20

PERMISSION_TYPE = (
    (SELF_ACCESS, "اجازه شخصی"),
    (FULL_ACCESS, "اجازه کل"),
)

permission_children = []


class PermissionRegister(type):
    def __new__(mcs, name, bases, classdict):
        new_cls = type.__new__(mcs, name, bases, classdict)
        if new_cls not in permission_children and new_cls.name and new_cls.id != 0:
            permission_children.append(new_cls)
        return new_cls


class Permission(metaclass=PermissionRegister):
    name = "اجازه"
    id = 0
    url = ''

    def __init__(self, user):
        self.user = user

    def check(self):
        pass

    def get_queryset(self):
        pass

    @staticmethod
    def get_permission_choices():
        choices = []
        for perm in permission_children:
            choices.append(
                (perm.id, perm.name)
            )
        return choices

    def get_url(self):
        return reverse(self.url)


class TimesPermission(Permission):
    name = "زمان ها!"
    id = 1
    code = 'times'

    def check(self):
        return True

    def get_queryset(self):
        if PermissionController.is_admin(self.user):
            return TimeSpend.objects.filter()
        if self.user.role.perms.filter(perm=TimesPermission.id, perm_type=SELF_ACCESS):
            return TimeSpend.objects.filter(account=self.user)
        elif self.user.role.perms.filter(perm=TimesPermission.id, perm_type=FULL_ACCESS):
            return TimeSpend.objects.filter()
        else:
            return TimeSpend.objects.none()


class PermissionController(object):
    @staticmethod
    def has_permission(user, perm):
        return perm(user).check()

    @staticmethod
    def get_queryset(user, perm):
        return perm(user).get_queryset()

    @staticmethod
    def is_admin(user):
        if user.is_authenticated() and user.is_superuser:
            return True
        return False


# DECORATOR FOR CHECK PERMISSION TO ACCESS DJANGO VIEW
def permission_required(perm):
    def permission_decorator(view):
        def wrapper(request, *args, **kwargs):
            if PermissionController.has_permission(request.user, perm):
                return view(request, *args, **kwargs)
            else:
                return HttpResponseForbidden()

        return wrapper

    return permission_decorator
