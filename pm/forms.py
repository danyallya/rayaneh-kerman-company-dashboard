from django import forms

from pm.models import Project, TimeSpend, WorkItem
from utils.forms import BaseForm


class TimeSpendForm(BaseForm):
    class Meta:
        model = TimeSpend
        fields = ('project', 'time_spend', 'desc', 'due_date')

    def __init__(self, *args, **kwargs):
        super(TimeSpendForm, self).__init__(*args, **kwargs)
        self.fields["due_date"].widget.attrs.update({'placeholder': u"مثال: 1394/04/13"})
        self.fields["time_spend"] = forms.CharField(max_length=255)
        self.fields["time_spend"].widget.attrs.update({'placeholder': u"مثال: 2.5 یا 2:30"})

    def clean(self):
        cd = super(TimeSpendForm, self).clean()
        time_spend = cd.get('time_spend')
        if time_spend:
            try:
                if ':' in time_spend:
                    hour, minutes = time_spend.split(":")
                    cd['time_spend'] = hour + "." + str(int(int(minutes) * 100 / 60))
                else:
                    float(time_spend)
            except Exception:
                self.errors['time_spend'] = self.error_class(["زمان وارد شده اشتباه است."])

        return cd


class ProjectForm(BaseForm):
    class Meta:
        model = Project
        fields = ('title', 'responsible')


class WorkItemForm(BaseForm):
    class Meta:
        model = WorkItem
        fields = ('title', 'account', 'project', 'desc', 'due_date', 'progress')
