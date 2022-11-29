from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

def homemorning(request):
    path = request.path
    # response = HttpResponse(path, content_type='text/html', charset='utf-8')
    response = HttpResponse("This works! ")
    return response


def myapphome(request):
    content = '<html><body style="background-color:orange;"><h1 style="color:blue;"> Hello, World! myapphome HOME PAGE  </h1></body></html>'
    return HttpResponse(content)


def myappabout(request):
    content = '<html><body style="background-color:yellow;"><h1 style="color:blue;"> Welcome to the ABOUT PAGE! </h1></body></html>'
    return HttpResponse(content)


def myapplittlelemonpage(request):
    content = '<html><body style="background-color:grey;"><h1 style="color:blue;"> Welcome to the Little Lemon restaurant PAGE! </h1></body></html>'
    return HttpResponse(content)


def say_hello(request):
    return HttpResponse(" 'Hello World' from the 'say_hello()' function! ")


def anotherfunction(request):
    return HttpResponse(" Greetings! from anotherfunction")


def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)


def menu(request):
    text = """<h1 style="color:#F4CE14;"> This is Little Lemon again! </h1>"""
    return HttpResponse(text)


def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is a type of noodle made from combination of different food',
        'falafel': 'Falafel are deep fried patties or balls made of ...',
        'cheesecake': 'Cheesecake is a type of dessert made with cheese ...'
    }

    description = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>" + description)


def fruititems(request, fruit):
    fruits = {
        'apple': 'Apple is a fruit',
        'orange': 'Orange is a fruit',
        'mango': 'Mango is a fruit'
    }

    description = fruits[fruit]
    return HttpResponse(f"<h2> {fruit} </h2>" + description)


def drinks(request, drink_name):
    drinks = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment'
    }
    choice_of_drink = drinks[drink_name]
    return HttpResponse(f"<h2> {drink_name} </h2>" + choice_of_drink)


def orders(request):
    text = """<h1 style="color:#F4CE14;">Welcom to the ORDER page! </h1>"""
    return HttpResponse(text)


def say_hello_7(request):
    return HttpResponse("Hello World from 'say_hello_7()' function ")
