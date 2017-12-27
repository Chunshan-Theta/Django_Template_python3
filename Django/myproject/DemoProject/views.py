# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import sys
sys.path.append('C:\\Users\\2017SEa\\Desktop\\Django_Template_python2-master\\Django\\myproject\\DemoProject\\models')
import MySQL_model
###### show view ######

def hello_world(request):
    template = 'hello_world.html'
    responds = {'stringData': str(datetime.now()),}
    return render(request,template,responds )


def UsingStaticSource(request):
    template = 'UsingStaticSource.html'
    responds = {}
    return render(request,template,responds )

def For_Cycle(request):
    template = 'For_Cycle.html'
    arr = [1,2,3,4,5,6,7,8,9]
    responds = {'Data':arr}
    return render(request,template,responds )

def Http_From_Get(request,input1,input2):
    template = 'hello_world.html'
    responds = {'stringData': str(input1)+str(input2),}
    return render(request,template,responds )

@csrf_exempt #csrf skip, if you want to get the http's post form anywhere
def Http_From_Post(request):
    try:
        data = str(request.POST['input1'])
    except KeyError as e:
        data = 'did not have post'


    template = 'Form.html'
    responds = {'stringData': data,}
    return render(request,template,responds )

@csrf_exempt #csrf skip, if you want to get the http's post form anywhere
def api_template(request):
    try:
        data = str(request.POST['input1'])
    except KeyError as e:
        data = 'did not have post'


    resp = HttpResponse(data)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp 
