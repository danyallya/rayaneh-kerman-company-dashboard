# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def intro(request):
    return render_to_response('intro.html', {}, context_instance=RequestContext(request))
