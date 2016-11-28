from django.http import HttpResponse
from django.shortcuts import render
import django.template

def test(request, *args, **kwargs):
    return HttpResponse("Hello, world. You're at the polls index.")

def temp(request, *args, **kwards):
	return render(request, 'qa/index.html')
