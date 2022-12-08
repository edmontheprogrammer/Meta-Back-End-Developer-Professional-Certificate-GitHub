from django.urls import path

from . import views

urlpatterns = [
    path('', views.myapphome),
    path('myapplittlelemonpage', views.myapplittlelemonpage),
    path('myappabout', views.myappabout),
    path('say_hello', views.say_hello),
    path('anotherfunction', views.anotherfunction),
    path('display_date', views.display_date),
    path('menu/', views.menu),
    path('orders', views.orders),
    path('say_hello_7', views.say_hello_7),
    path('homemorning', views.homemorning),
    path('dishes/<str:dish>', views.menuitems),
    path('fruits/<str:fruit>', views.fruititems),
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
    path('form_home/', views.form_view, name="form_home"),

]
