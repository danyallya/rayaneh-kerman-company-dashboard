from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse
from django.db.models.aggregates import Sum
from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from account.models import Account

from account.permissions import PermissionController, TimesPermission
from pm.forms import TimeSpendForm, ProjectForm, WorkItemForm
from pm.models import TimeSpend, WorkItem


@login_required
def times(request):
    if not PermissionController.has_permission(request.user, TimesPermission):
        return HttpResponseForbidden()

    ts = PermissionController.get_queryset(request.user, TimesPermission)

    p = request.GET.get('p')
    u = request.GET.get('u')
    i = request.GET.get('i')
    if p:
        if p == '0':
            ts = ts.filter(project__isnull=True)
        else:
            ts = ts.filter(project__id=p)
    if u:
        ts = ts.filter(account__id=u)
    if i:
        ts = ts.filter(due_date=i)

    ts = ts.order_by('-due_date')

    ts_sum = ts.aggregate(Sum('time_spend'))['time_spend__sum'] or 0

    ts_sum = "%.2f" % round(ts_sum, 2)

    form = TimeSpendForm()
    edit_form = TimeSpendForm(prefix="edit")
    project_form = ProjectForm()
    if request.method == 'POST':
        if request.POST.get('title'):
            project_form = ProjectForm(request.POST)
            if project_form.is_valid():
                project_form.save()
                project_form = ProjectForm()
        else:
            form = TimeSpendForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.account = request.user
                obj.creator = request.user
                obj.save()
                form = TimeSpendForm()

    return render(request, 'pm/times.html',
                  {'times': ts, 'form': form, 'project_form': project_form, 'edit_form': edit_form,
                   'users': Account.objects.all(), 'ts_sum': ts_sum})


@login_required
def edit_time(request, time_id):
    obj = get_object_or_404(TimeSpend, id=time_id)
    if request.method == 'POST' and obj.account_id == request.user.id:
        form = TimeSpendForm(request.POST, prefix="edit", instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.account = request.user
            obj.creator = request.user
            obj.save()
    return HttpResponseRedirect(reverse('times'))


@login_required
def delete_time(request, time_id):
    obj = get_object_or_404(TimeSpend, id=time_id)
    if obj.account_id == request.user.id:
        obj.delete()
    return HttpResponseRedirect(reverse('times'))


@login_required
def work_list(request):
    # if not PermissionController.has_permission(request.user, TimesPermission):
    #     return HttpResponseForbidden()

    # ts = PermissionController.get_queryset(request.user, TimesPermission)
    form = WorkItemForm()

    if request.method == 'POST':
        form = WorkItemForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.creator = request.user
            obj.save()
            form = WorkItemForm()

    works = WorkItem.objects.filter()

    return render(request, 'pm/times.html', {'works': works, 'form': form})
