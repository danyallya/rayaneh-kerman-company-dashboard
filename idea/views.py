# -*- coding:utf-8 -*-
from django.shortcuts import render


def idea_list(request):
    return render(request, 'idea/list.html', {})


def idea_page(request):
    return render(request, 'idea/page.html', {})
