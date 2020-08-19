"""Platzigram views"""
from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime
import json


def hello(request):
    return HttpResponse('oh, Hi current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - &H:%M hrs')
    ))


def sorted(request):
    numbers = sorted([int(i) for i in request.GET['numbers'].split(',')])
    responseData = {
        'status': 'ok',
        'numbers': numbers,
        'message': 'Integeres parsed succesfuly'
    }
    return HttpResponse(json.dumps(responseData))

def say_hi(request,name,age):

    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {} you are allowed'.format(name)

    return HttpResponse(message)