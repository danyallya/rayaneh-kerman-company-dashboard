# -*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from idea.models import Idea
from utils.forms import BaseForm


class IdeaForm(BaseForm):
    class Meta:
        model = Idea
        fields = ('title', 'brief', 'first_desc', 'economic_justification')


@login_required
def idea_list(request):
    ideas = Idea.objects.filter().order_by('-id')

    form = IdeaForm()

    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.creator = request.user
            obj.save()
            form = IdeaForm()

    return render(request, 'idea/list_idea.html', {'ideas': ideas, 'form': form})


@login_required
def idea_page(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)

    return render(request, 'idea/page.html', {'idea': idea})
