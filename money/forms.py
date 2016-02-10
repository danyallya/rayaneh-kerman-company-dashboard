from django import forms
from money.models import BankAccount, Transaction

__author__ = 'M.Y'

from utils.forms import BaseForm


class BankForm(BaseForm):
    class Meta:
        model = BankAccount
        fields = ('title', 'account_num')


class TransactionForm(BaseForm):
    class Meta:
        model = Transaction
        fields = ('pay_type', 'money_type', 'desc', 'code', 'amount', 'person', 'date')

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields["date"].widget.attrs.update({'placeholder': u"مثال: 1394/04/13"})
        self.fields["desc"].widget.attrs.update({'rows': '2'})
