from django.conf import settings
from django import forms
from django.contrib.auth import (
    login as django_login, authenticate,
    logout as django_logout
)
from django.core.mail import send_mail
from django.shortcuts import (
    render, redirect, render_to_response,
    resolve_url, get_object_or_404
)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView
from django.views.generic import DetailView, ListView, UpdateView
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import generics

from Auth.serializers import *
from Auth.forms import *
from Auth.models import User
from elfsyndicate.settings import LOGIN_URL

class UserAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


def login(request):
    if request.user.is_authenticated():
        return redirect('/accounts/profile/%s' % request.user.username)
    form = AuthenticationForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            django_login(request, user)
            return redirect('/accounts/profile/%s' % user.username)
    return render(request, 'auth/login.html', {'form': form})

@sensitive_post_parameters("password")
def register(request):
    if request.user.is_authenticated():
        redirect('/accounts/profile/%s' % request.user.username)
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            django_login(request, user)
            return redirect('/accounts/profile/%s' % user.username)
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})

@login_required(login_url='/accounts/login/')
def logout(request):
    django_logout(request)
    return redirect('/accounts/login/')

def get_user_profile(request, username):
    try:
        user = User.objects.get(username__iexact=username)
    except User.DoesNotExist:
        user = None
    return render(request, 'auth/profile.html', {'user': user})

@login_required(login_url=LOGIN_URL)
def user_profile_edit(request, username):
    user = request.user
    if request.user.username == user.username:
        if request.method == 'POST':
            uform = UserForm(request.POST, instance=request.user)
            pform = ProfileForm(request.POST, instance=request.user.profile)
            if uform.is_valid() and pform.is_valid():
                uform.save()
                pform.save()
        else:
            uform = UserForm(instance=request.user)
            pform = ProfileForm(instance=request.user.profile)
        return render(request, 'auth/profile_edit.html', {
            'uform': uform,
            'pform': pform
        })
    else:
        # If requesting user tries to edit another users profile
        return redirect('/accounts/profile/%s' % user.username)
    return redirect(request, '/accounts/profile/edit/%s' % user.username)
