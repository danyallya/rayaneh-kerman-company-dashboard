from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from pm.models import TimeSpend


class TimeSpendForm(forms.ModelForm):
    class Meta:
        model = TimeSpend
        fields = ('project', 'time_spend', 'desc')


@login_required
def times(request):
    ts = TimeSpend.objects.all()
    if request.method == 'POST':
        form = TimeSpendForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.account = request.user
            obj.save()
    else:
        form = TimeSpendForm()
    return render(request, 'pm/times.html', {'times': ts, 'form': form})
