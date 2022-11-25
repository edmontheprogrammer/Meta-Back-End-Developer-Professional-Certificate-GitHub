from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# This is our view function.


def demoappHome(request):
    content = '<html><body style="background-color:green;"><h1 style="color:brown;">Hello, world. This is the index of the Demoapp.</h1></body></html>'
    return HttpResponse(content)
