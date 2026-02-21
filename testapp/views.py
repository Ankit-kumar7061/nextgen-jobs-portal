from django.shortcuts import render
from testapp.models import *

def index(request):
    return render(request,'testapp/index.html')


def hydjobs_view(request):
    jobs_list = hydjobs.objects.order_by('date')
    return render(request,'testapp/hydjobs.html',{'jobs_list':jobs_list})


def blorejobs_view(request):
    jobs_list = blorejobs.objects.order_by('date')
    return render(request,'testapp/blorejobs.html',{'jobs_list':jobs_list})


def chennaijobs_view(request):
    jobs_list = chennaijobs.objects.order_by('date')
    return render(request,'testapp/chennaijobs.html',{'jobs_list':jobs_list})


def punejobs_view(request):
    jobs_list = punejobs.objects.order_by('date')
    return render(request,'testapp/punejobs.html',{'jobs_list':jobs_list})