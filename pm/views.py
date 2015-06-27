from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from pm.models import TimeSpend, Project

from utils.forms import BaseForm


class TimeSpendForm(BaseForm):
    class Meta:
        model = TimeSpend
        fields = ('project', 'time_spend', 'desc', 'due_date')
    def __init__(self, *args, **kwargs):
        super(TimeSpendForm, self).__init__(*args, **kwargs)
        self.fields["due_date"].widget.attrs.update({'placeholder': u"مثال: 13/04/1394"})

class ProjectForm(BaseForm):
    class Meta:
        model = Project
        fields = ('title', 'responsible')


@login_required
def times(request):
    p = request.GET.get('p')
    u = request.GET.get('u')
    i = request.GET.get('i')
    ts = TimeSpend.objects.filter().order_by('-id')
    if p:
        if p == '0':
            ts = ts.filter(project__isnull=True)
        else:
            ts = ts.filter(project__id=p)
    if u:
        ts = ts.filter(account__id=u)
    if i:
        ts = ts.filter(due_date=i)
    form = TimeSpendForm()
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
    return render(request, 'pm/times.html', {'times': ts, 'form': form, 'project_form': project_form})
