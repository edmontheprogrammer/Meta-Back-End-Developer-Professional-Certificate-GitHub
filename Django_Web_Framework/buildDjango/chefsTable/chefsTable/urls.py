"""chefsTable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from myapp import views

# Note 1: http://127.0.0.1:2000/ ---> maps to '' or home page
# So empty strings, '' , defaults to the localhost or 127.0.0.1 plus
# the port number
# Note 2: http://127.0.0.1:2000/demo/ ---> maps to 'demo'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'), name='myapp-home'),
    path('demoapp_home/', include('demoapp.urls'), name='demoapp-home'),
    path('mysecondapp_home/', include('mysecondapp.urls'), name='mysecondapp-home'),
    # path('myapp_home', views.myapphome, name='myapp-home'),
    # path('myapp_about', views.myappabout, name='myapp-about'),
    # path('myapp_littlelemon', views.myapplittlelemon,
    #     name='myapp-little-lemon-restaurant'),
]
