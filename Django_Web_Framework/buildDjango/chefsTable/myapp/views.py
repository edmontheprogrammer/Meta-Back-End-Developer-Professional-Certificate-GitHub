from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def myapphome(request):
    content = '<html><body style="background-color:orange;"><h1 style="color:blue;"> Hello, World! </h1></body></html>'
    return HttpResponse(content)


def myappabout(request):
    content = '<html><body style="background-color:yellow;"><h1 style="color:blue;"> Welcome to the about page! </h1></body></html>'
    return HttpResponse(content)


def myapplittlelemonHome(request):
    content = '<html><body style="background-color:grey;"><h1 style="color:blue;"> Welcome to the Little Lemon restaurant! </h1></body></html>'
    return HttpResponse(content)
