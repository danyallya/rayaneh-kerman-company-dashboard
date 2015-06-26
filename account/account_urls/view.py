from django.conf.urls import patterns, url

from prk.account.models import Account, AccountRole, AccountTeam
from prk.account.views.account import ListAccountView
from prk.account.tables import AccountTable, AccountRoleTable, AccountTeamTable


urlpatterns = patterns('',
    url(r'^item',
        ListAccountView.as_view(
            queryset=Account.objects.all(),
            model=Account,
            table=AccountTable,
            page_title = 'Accounts',
            page_heading = 'Accounts:',
        ),
        name='item'),

    url(r'^role',
        ListAccountView.as_view(
            queryset=AccountRole.objects.all(),
            model=AccountRole,
            table=AccountRoleTable,
            page_title = 'Account Roles',
            page_heading = 'Account Roles:',
        ),
        name='role'),

    url(r'^team',
        ListAccountView.as_view(
            queryset=AccountTeam.objects.all(),
            model=AccountTeam,
            table=AccountTeamTable,
            page_title = 'Account Teams',
            page_heading = 'Account Teams:',
        ),
        name='team'),
)