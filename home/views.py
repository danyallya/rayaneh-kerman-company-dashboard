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


def about(request):
    return render_to_response('about.html')


def work_page(request):
    return render_to_response('work_page.html')


def account_list(request):
    return render_to_response('money/account_list.html')


def account_page(request):
    return render_to_response('money/account_page.html')


def post_list(request):
    return render_to_response('post_list.html')


def post_page(request):
    return render_to_response('post_page.html')


def talk(request):
    return render_to_response('talk.html')


def work_list(request):
    return render_to_response('work_list.html')


def my_money(request):
    return render_to_response('money/my_money.html')


def resume(request):
    return render_to_response('apps/resume.html')
def blog_list(request):
    return render_to_response('blog_list.html')


def blog_page(request):
    return render_to_response('blog_page.html')