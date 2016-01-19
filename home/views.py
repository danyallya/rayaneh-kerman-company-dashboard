# -*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from utils.messages import ContactEmail


def intro(request):
    return render(request, 'intro.html', {})


def contact(request):
    name = request.POST.get('n')
    email = request.POST.get('e')
    title = request.POST.get('t')
    text = request.POST.get('te')

    ContactEmail(name, email, title, text).start()

    return HttpResponse("OK")


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


def my_idea(request):
    return render_to_response('my_idea.html')


def mahsool(request):
    return render_to_response('mahsool.html')


def list_mahsool(request):
    return render_to_response('list_mahsool.html')


def project(request):
    return render_to_response('project.html')
