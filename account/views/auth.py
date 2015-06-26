# -*- coding:utf-8 -*-
from django.core.urlresolvers import reverse

__author__ = 'M.Y'
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext


class SignInForm(forms.Form):
    username = forms.CharField(label=u"نام کاربری",
                               widget=forms.TextInput(
                                   {'placeholder': u'نام کاربری'}))
    password = forms.CharField(label=u"گذرواژه",
                               widget=forms.PasswordInput(
                                   {'placeholder': u'گذرواژه'}))


ignore_next_pages = ['signup']


def login(request):
    from django.contrib.auth import authenticate, login

    if request.method == 'POST':
        login_form = SignInForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is None or not user.is_active:
                messages.error(request, u"نام کاربری یا گذرواژه نادرست است.")
            else:

                login(request, user)
                next_page = request.GET.get('next')
                for page in ignore_next_pages:
                    if page in next_page:
                        next_page = '/'
                        break

                if next_page:
                    return HttpResponseRedirect(next_page)
                else:
                    return HttpResponseRedirect('/admin')
    else:
        login_form = SignInForm()

    context = {
        'title': u"ورود به دیبا",
        'app_path': request.get_full_path(),
        'next': request.get_full_path(),
        'form': login_form
    }
    return render_to_response('login.html', context,
                              context_instance=RequestContext(request))


def signup(request):
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST.copy())
    #     if form.is_valid():
    #         form.save()
    #         next = request.GET.get('next')
    #         if next:
    #             return HttpResponseRedirect(reverse('next'))
    #
    #         return HttpResponseRedirect(reverse('login'))
    # else:
    #     form = SignUpForm()
    return render(request, 'accounts/edit.html', {'form': ''})


def logout(request):
    from django.contrib.auth import logout

    logout(request)
    return HttpResponseRedirect(reverse('index'))
