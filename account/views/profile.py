# -*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


__author__ = 'M.Y'


@login_required
def show_profile(request):
    # user = request.user
    # profile = Profile.objects.get_or_create(user_id=user.id)[0]
    return render(request, 'accounts/show.html', {'profile': ''})


@login_required
def edit_profile(request):
    # user = request.user
    # profile = Profile.objects.get_or_create(user_id=user.id)[0]
    # if request.method == 'POST':
    #     form = ProfileForm(request.POST.copy(), instance=profile)
    #     if form.is_valid():
    #         form.save()
    #         form = ProfileForm(instance=profile)
    # else:
    #     form = ProfileForm(instance=profile)
    return render(request, 'accounts/edit.html', {'profile': '', 'form': ''})
