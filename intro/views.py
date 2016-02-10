# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext


def intro(request):
    return render_to_response('intro.html', {}, context_instance=RequestContext(request))


def delnev(request):
    return render(request, 'apps/del.html', {})


def finite(request):
    return render(request, 'apps/finite.html', {})
