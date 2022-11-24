from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# This is our view function.


def index(request):
    content = "<html><body><h1>Hello, world. This is the index of the Demoapp.</h1></body></html>"
    return HttpResponse(content)
