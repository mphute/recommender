from django.http import HttpResponse
from django.shortcuts import render


def bookrec(request):
        context = {'foo': 'bar'}
        return render(request,'bookrec.html',context = context)


def bookcover(request):
        context = {'foo': 'bar'}
        return render(request,'bookcover.html',context = context)

def movierec(request):
        context = {'foo': 'bar'}
        return render(request,'movierec.html',context = context)

def moviecover(request):
        context = {'foo': 'bar'}
        return render(request,'moviecover.html',context = context)