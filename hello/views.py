from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import escape
from django.views import View
from django.urls import reverse

def cookies(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    resp = HttpResponse('view count='+str(num_visits))
    resp.set_cookie('dj4e_cookie', '7ae738bc', max_age=1000)
    resp.set_cookie('chocolate','hash')
    return resp

# https://www.youtube.com/watch?v=Ye8mB6VsUHw

def sessfun(request) :
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits 
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    return resp
