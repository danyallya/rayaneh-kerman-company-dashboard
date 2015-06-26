# -*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

@login_required
def index(request):
    return render_to_response(
        'index.html',
        {},
        context_instance=RequestContext(request))


def get_images(request):
    import urllib

    # for i in range(817, 900):
    #     f = open('c:/b/%s.jpg' % i, 'wb')
    #     f.write(
    #         urllib.urlopen(
    #             'http://library.sharif.ir/parvan/resource/292375/c/19942/get/dsPID=ma%s&scale=1.7' % i).read())
    #     f.close()

    return HttpResponse("OK")