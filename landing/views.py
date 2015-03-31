from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.template.response import TemplateResponse


def landing(request):
    return HttpResponse('<p> Hello </p>')


def test(request):
    messages.success(request, 'bootstrap3, twitter_bootstrap & pipeline working. ')
    messages.success(request, 'animate, hover-min and css3-animate-it working')
    return TemplateResponse(request, 'test.html', context={})