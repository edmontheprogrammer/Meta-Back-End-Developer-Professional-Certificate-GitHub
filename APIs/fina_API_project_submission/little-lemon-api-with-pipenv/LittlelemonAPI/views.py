from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle


from .models import Categories, MenuItems, Orders


@api_view()
def categories(request):
    categories = Categories.objects.all()
    return Response(categories.values())


@api_view()
def menu_items(request):
    items = MenuItems.objects.all()
    menu_name = request.query_params.get('title')
    to_price = request.query_params.get('price')
    search = request.query_params.get('search')
    perpage = request.query_params.get('perpage', default=2)
    page = request.query_params.get('page', default=1)

    if menu_name:
        items.filter(menu_item__title=menu_name)
    if to_price:
        items = items.filter(price__lte=to_price)
    if search:
        items = items.filter(title__icontains=search)
    paginator = Paginator(items, per_page=perpage)
    try:
        items = paginator.page(number=page)
    except EmptyPage:
        items = []
    return Response(items.values())


@api_view()
def orders(request):
    orders = Orders.objects.all()
    order_totals = request.query_params.get('total')
    order_date = request.query_params.get('date')
    search = request.query_params.get('search')
    perpage = request.query_params.get('perpage', default=2)
    page = request.query_params.get('page', default=1)

    if order_totals:
        orders.filter(total__lte=order_totals)
    if order_date:
        order_date = orders.filter(date__lte=order_date)
    if search:
        orders = orders.filter(title__icontains=search)
    paginator = Paginator(orders, per_page=perpage)
    try:
        orders = paginator.page(number=page)
    except EmptyPage:
        orders = []

    return Response(orders.values())


@api_view()
@throttle_classes([AnonRateThrottle])
@throttle_classes([UserRateThrottle])
def throttle_check(request):
    return Response({"message": "successful"})


# @api_view()
# def order_items(request):
#     order_items = OrderItems.objects.all()
#     return Response(order_items.values())


# Create your views here.
# Function or class-based views:
#
# You can use function- or class-based views or both in this project. Follow the proper API
# naming convention throughout the project. Review the video about
# "Function and class-based views" as well as the video about "Naming convention" ##

# API Get request ##


# @api_view()
# def littlelemons(request):
#     return Response("list of littlelemons", status=status.HTTP_200_OK)

# API Post request ##


# @api_view(['POST'])
# def littlelemons(request):
#     return Response("list of littlelemons", status=status.HTTP_200_OK)

# Error Check and Proper status codes:
# You are required to display error messages with appropriate HTTP status codes for specific
# errors. These include when someone requests a non-existing item, makes unauthroized API
# request a non-existing item, makes unauthorized API requests, or sends invalid data in a
# "POST", "PUT" or "PATCH" request. Here is a full list.  ##


class Littlelemon(APIView):
    def get(self, request):
        return Response({"message": "list of littlelemons"}, status.HTTP_200_OK)

    def post(self, request):
        return Response({"title": request.data.get('title')}, status.HTTP_201_CREATED)

    # def unauthorized(self, request):
    #     return Response({"message": "authorization failed for the current user token"}, status.HTTP_403_UNAUTHORIZED)

    # def forbidden(self, request):
    #     return Response({"message": "authentication failed"}, status.HTTP_401_FORBIDDEN)

    # def badrequest(self, request):
    #     return Response({"message": "validation failed for 'POST', 'PUT', 'PATCH' or 'DELETE' call "}, status.HTTP_400_BAD_REQUEST)

    # def notfound(self, request):
    #     return Response({"message": "request was made for a non-existing resource"}, status.HTTP_404_NOT_FOUND)


# Codes for "serializers" of "Category model" in models.py file
