from django.shortcuts import render
from django.conf import settings
from django import forms
from django.shortcuts import (
    render, redirect, render_to_response, resolve_url, get_object_or_404
)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView
from django.views.generic import DetailView, ListView, UpdateView
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.utils import timezone
from rest_framework import generics

from character.serializers import CharacterSerializer
from character.forms import *
from character.models import *
from Auth.models import User
from elfsyndicate.settings import LOGIN_URL

class CharacterApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

@login_required(login_url=LOGIN_URL)
def character_create(request):
    user = request.user
    if request.method == 'POST':
        form = CreationForm(data=request.POST)
        if form.is_valid():
            player = user
            character = form.save(commit=False)
            character.player = player
            character.save()
            return redirect('/characters/character/%s/%s' % (character.pk, character.c_name))
    else:
        form = CreationForm()
    return render(request, 'character/create.html', {
        'form': form, 'user': user
    })

def character_detail(request, pk, c_name):
    c_name = Character.objects.get(c_name__iexact=c_name)
    try:
        char = Character.objects.get(pk=pk)
        inv = Inventory.objects.get(character=char)
    except Character.DoesNotExist:
        char = None
        inv = None
        return redirect('/404/')
    return render(request, 'character/character-detail.html', {
        'char': char,
        'inv': inv
    })

@login_required(login_url=LOGIN_URL)
def character_edit(request, c_name, pk):
    c_name = Character.objects.get(c_name__iexact=c_name)
    user = request.user
    char = Character.objects.get(pk=pk)
    if request.user.username == user.username:
        if request.method == 'POST':
            inv = Inventory.objects.get(character=char)
            cform = CharEditForm(request.POST)
            iform = InvEditForm(request.POST)
            if cform.is_valid() and iform.is_valid():
                cform.save()
                iform.save()
        else:
            cform = CharEditForm()
            iform = InvEditForm()
        return render(request, 'character/character-edit.html', {
            'cform': cform,
            'iform': iform
        })
    else:
        return redirect('/characters/character/%s' % char.c_name)
    return redirect(request, '/characters/character/edit/%s' % char.c_name)

def handler404(request):
    response = render_to_response('404.html', {},
                context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html', {},
                context_instance=RequestContext(request))
    response.status_code = 500
    return response
