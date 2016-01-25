# -*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from money.forms import BankForm, TransactionForm
from money.models import BankAccount, Transaction


@login_required
def bank_list(request):
    banks = BankAccount.objects.all()

    last_trans = Transaction.objects.filter().order_by('-id')[:10]

    form = BankForm()

    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.creator = request.user
            obj.save()
            form = BankForm()

    return render(request, 'money/account_list.html', {'banks': banks, 'form': form, 'last_trans': last_trans})


@login_required
def bank_page(request, bank_id):
    bank_account = get_object_or_404(BankAccount, id=bank_id)

    transactions = Transaction.objects.filter(bank_account=bank_account).order_by('-date')

    form = TransactionForm()

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.creator = request.user
            obj.bank_account = bank_account
            obj.save()
            form = TransactionForm()

    return render(request, 'money/account_page.html',
                  {'bank': bank_account, 'form': form, 'transactions': transactions})
