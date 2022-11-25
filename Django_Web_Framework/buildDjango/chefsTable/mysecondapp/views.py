from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def mysecondapphome(request):
    content = '<html><body style="background-color:purple" ><h1>This is the mysecondapp Home Page </h1> </body> </html>'
    return HttpResponse(content)
